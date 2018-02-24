import tweepy
from tweet import Tweet
import time

class stream_listener(tweepy.StreamListener):

    def __init__(self, tweets, max_tweets):
        self.tweets = tweets
        self.max_tweets = max_tweets
        self.curr_tweets = 0
        self.start = time.time()

    def on_data(self, data):
        elapsed = time.time() - self.start
        if (self.curr_tweets < self.max_tweets):
            try:
                parsed_tweet = Tweet(data)
            except KeyError as e:
                return True

            if parsed_tweet.lang == "en" and not parsed_tweet.truncated:
                self.tweets.append(parsed_tweet)
                self.curr_tweets += 1
                print "Tweets collected: " + str(self.curr_tweets)

            return True
        else:
            print "%d tweets collected in %d seconds" % (self.curr_tweets, elapsed)
            return False

    def on_error(self, status):
        print "Error, " + str(status)
        return False
