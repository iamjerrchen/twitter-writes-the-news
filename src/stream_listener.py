import tweepy
import time

class stream_listener(tweepy.StreamListener):

	def __init__(self, tweets, max_tweets, timeout):
		self.tweets = tweets
		self.max_tweets = max_tweets
		self.timeout = timeout
		self.curr_tweets = 0
		self.start = time.time()

	def on_data(self, data):
		if (self.curr_tweets < self.max_tweets) and (time.time() - self.start < self.timeout):
			self.tweets.append(data)
			self.curr_tweets += 1

			print "Tweets collected: " + str(self.curr_tweets)

			return True
		else:
			print "All tweets collected"
			return False

	def on_error(self, status):
		print "Error, " + str(status)
		return False
