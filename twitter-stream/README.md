# Docker FTW twitter-stream

Application that listens on hashtags and prints to stdout or bombs a set of tweets out
to the public twitter world.

### Requirements:

* Docker: [https://www.docker.com](https://www.docker.com)

### Build:

* `docker build -t twitter-stream .`

### Environment Variable Configuration:

* PORT:
    * The port the healthcheck webserver runs on
* TRACKS:
    * set environment variables to listen on custom track. eg (TRACKS=dockerftw,docker)
* BLAST:
    * set environment variable BLAST=True if you want to tweet out a blast of tweets
* TWEET_COUNT:
    * how many tweets to send. This defaults to 3
* TWEET_MSG:
    * a configurable message to send vs the default.
* RETWEET:
    * if set to True, then we retweet the status.
* IGNORE_USERS:
    * ignore csv list of users to retweet. This is usually for the account that is retweeting, so we dont error 
    on every single RT. Could be for other use cases as well.
* REPLY:
    * If set to True, then all tweets that are found in the track will be responded too. with "@username WOW... That is so interesting!!!"
* REPLY_MSG:
    * if set, then the reply message will be what you pass in.
* DELETE_TWEETS:
    * If set to True, then all tweets will be deleted from account. Use with caution. This is so we can clean up after tweeting a whole bunch of crapola. 
* LANGUAGES:
    * Set the language filter. Allow for multiple languages, which is a csv of languages. Default is "en"
* Twitter API keys:
    * Go to [http://apps.twitter.com](http://apps.twitter.com) and create an application to get the `consumer_key`, `consumer_secret`, `access_token_key` and `access_token_secret`
    * Then set these values as docker env-file
* RESET_BLOCKED_COUNT
    * set to have the bot reset the number of tweets it sees before requesting for blocked users. This should be higher if you are following tracks that are tweeted many times. If not you will get throttled by the twitter apis. 
    * default is 10
    
#### Note on blocked users
If a user is blocked from the account that is tweeting, then that blocekd users will not get retweeted or replied too. This allows you to easily block users from twitter application and then have the bot still adhere to those blocks. 

### Run Listener:
* ```docker run -it --env-file=./twitter.secrets -e TRACKS=docker,dockerftw twitter-stream```

### Run Blaster
* ```docker run -it --env-file=./twitter.secrets -e BLAST=True -e TRACKS=docker,dockerftw twitter-stream```

### Stop:

* `docker stop twitter-stream`

### Credits:

* Tweepy: [https://github.com/tweepy/tweepy](https://github.com/tweepy/tweepy)
* twitter-stream: [https://github.com/rferrerme/twitter-stream](https://github.com/rferrerme/twitter-stream)
