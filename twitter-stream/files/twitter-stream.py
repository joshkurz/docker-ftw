import os, sys, traceback
import time
from tweepy.streaming import Stream, StreamListener
from tweepy import OAuthHandler, API, TweepError
from tweepy.utils import import_simplejson

json = import_simplejson()

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_SECRET_TOKEN")

if not consumer_key or not consumer_secret or not access_token or not access_token_secret:
    print "Must provide all secret environment variables"
    sys.exit(1)
 
# Tracks to listen too
tracks = os.getenv('TRACKS', "docker, dockerftw").split(',')
blast = os.getenv('BLAST', False)
delete = os.getenv('DELETE_TWEETS', False)
reply = os.getenv('REPLY', False)
reply_msg = os.getenv('REPLY_MSG', "Wow... That is so interesting!!!")
retweet = os.getenv('RETWEET', False)
ignore_users = os.getenv('IGNORE_USERS', 'dockerftw').split(',')
tweet_count = int(os.getenv('TWEET_COUNT', 3))
tweet_msg = os.getenv('TWEET_MSG', '#dockerftw baby')
languages = os.getenv('LANGUAGES', 'en').split(',')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    
    def __init__(self):
        self.data_payloads = 0
        ## get blocked users
        print "getting blocked users"
        self.blocked = api.blocks_ids().get("ids")
        print self.blocked

    def on_data(self, data):
        self.data_payloads += 1
        tweet = json.loads(data)
        username = tweet.get("user", {}).get("screen_name", "").encode('utf-8').strip()
        text = tweet.get("text", "").encode('utf-8').strip()
        _id = tweet.get("id", "")
        print "@%s: %s" % (username, text)
        
        if self.data_payloads > 20:
            self.blocked = api.blocks_ids().get("ids")
            self.data_payloads = 0
            
        # if retweet is set
        if retweet == "True" and username not in ignore_users and _id not in self.blocked:
            try:
                api.retweet(id=tweet.get("id"))
                print "Retweeted Tweet %s" % (tweet.get("id"))
            except TweepError as e:
                print e.message[0]['message']
            
        # if reply is set
        if reply == "True" and username not in ignore_users and _id not in self.blocked:
            try:
                reply_text = "@%s %s" % (username, reply_msg)
                api.update_status(status=reply_text, in_reply_to_status_id=tweet.get("id"))
                print "Replied to Tweet %s" % (tweet.get("id"))
            except TweepError as e:
                print e.message[0]['message']
            
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    try:
        
        if delete == "True":
            # delete all tweets
            data = api.home_timeline(count=800)
            for tweet in data:
                if tweet.retweeted == False:
                    try:
                        api.destroy_status(tweet.id)
                        print "Deleted %s" % (tweet.text.encode('utf-8').strip())
                    except:
                        continue
            
        if blast == "True":
            count = 0
            while True:
                count = count + 1
                tweet = "%s %s" % (tweet_msg, count)
                print "Tweeting %s" % (tweet)
                time.sleep(1)  # Delay for 1 second
                api.update_status(status=tweet)
                if count > tweet_count:
                    print "Done Tweeting"
                    sys.exit(1)
        else:
            l = StdOutListener()
            stream = Stream(auth, l)
            print "Listening to twitter tracks: %s in %s" % (tracks, languages)
            stream.filter(languages=languages, track=tracks)
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
