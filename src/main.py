import argparse
import parser
import ConfigParser
from stream_listener import stream_listener
from tweet import Tweet
import tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

CONFIG="configuration/keys.ini"
def main():

	# Parse arguments from command line
    args = parser.get_args()
    config = ConfigParser.ConfigParser()

    if args.keywords is None or len(args.keywords) == 0:
        raise argparse.ArgumentTypeError("No keywords!")

    # Read in from Config file
    config.read(CONFIG)
    consumer_key = config.get("keys", "ConsumerKey")
    consumer_secret = config.get("keys", "ConsumerSecret")
    access_token = config.get("keys", "AccessToken")
    access_secret = config.get("keys", "AccessSecret")

    # Verify credentials
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    # Collect tweets based on arguments (or default vals)
    tweets = []
    streamListener = stream_listener(tweets, args.max_tweets)
    stream = tweepy.Stream(auth=auth, listener=streamListener, timeout=args.timeout*60)

    print "Collecting tweets..."
    stream.filter(track=args.keywords)

    # TEST: print tweets
    for twt in tweets:
        twt.disp()
        print

if __name__ == '__main__':
    main()


