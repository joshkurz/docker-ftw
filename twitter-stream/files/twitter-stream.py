import os, sys, traceback
import time
from tweepy.streaming import Stream, StreamListener
from tweepy import OAuthHandler, API
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
tracks = os.getenv('TRACKS', "docker, dockerftw")
blast = os.getenv('BLAST', False)

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        tweet = json.loads(data)
        username = tweet.get("user", {}).get("screen_name", "").encode('utf-8').strip()
        text = tweet.get("text", "").encode('utf-8').strip()
        print "@%s: %s" % (username, text)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        if blast == "True":
            api = API(auth)
            count = 0
            while True:
                count = count + 1
                tweet = "#dockerftw baby %s" % (count)
                print "Tweeting %s" % (tweet)
                time.sleep(1)  # Delay for 1 second
                api.update_status(status=tweet)
                if count == 3:
                    print "Done Tweeting"
                    sys.exit(1)
        else:
            l = StdOutListener()
            stream = Stream(auth, l)
            print "Listening to twitter tracks: %s" % (tracks)
            stream.filter(track=[tracks])
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
