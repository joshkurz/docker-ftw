# Docker FTW twitter-stream

Application that listens on hashtags and prints to stdout or bombs a set of tweets out
to the public twitter world.

### Requirements:

* Docker: [https://www.docker.com](https://www.docker.com)

### Build:

* `docker build -t twitter-stream .`

### Environment Variable Configuration:

* TRACKS:
    * set environment variables to listen on custom track. eg (TRACKS=dockerftw,docker)
* BLAST:
    * set environment variable BLAST=True if you want to tweet out a blast of tweets
* TWEET_COUNT:
    * how many tweets to send. This defaults to 3
* TWEET_MSG:
    * a configurable message to send vs the default.
* REPLY:
    * If set to True, then all tweets that are found in the track will be responded too. with "@username WOW... That is so interesting!!!"
* REPLY_MSG:
    * if set, then the reply message will be what you pass in.
* DELETE_TWEETS:
    * If set to True, then all tweets will be deleted from account. Use with caution. This is so we can clean up after tweeting a whole bunch of crapola. 
* Twitter API keys:
    * Go to [http://apps.twitter.com](http://apps.twitter.com) and create an application to get the `consumer_key`, `consumer_secret`, `access_token_key` and `access_token_secret`
    * Then set these values as docker env-file

### Run Listener:
* ```docker run -it --env-file=./twitter.secrets -e TRACKS=docker,dockerftw twitter-stream```

### Run Blaster
* ```docker run -it --env-file=./twitter.secrets -e BLAST=True -e TRACKS=docker,dockerftw twitter-stream```

### Stop:

* `docker stop twitter-stream`

### Credits:

* Tweepy: [https://github.com/tweepy/tweepy](https://github.com/tweepy/tweepy)
* twitter-stream: [https://github.com/rferrerme/twitter-stream](https://github.com/rferrerme/twitter-stream)