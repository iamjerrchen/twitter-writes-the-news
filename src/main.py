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
    args = parser.get_args()
    config = ConfigParser.ConfigParser()

    # Config 
    config.read(CONFIG)
    consumer_key = config.get("keys", "ConsumerKey")
    consumer_secret = config.get("keys", "ConsumerSecret")
    access_token = config.get("keys", "AccessToken")
    access_secret = config.get("keys", "AccessSecret")

    # Verify credentials
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    if args.keywords is None or len(args.keywords) == 0:
        raise argparse.ArgumentTypeError("No keywords!")

    # Testing stream listener
    tweets = []
    testListener = stream_listener(tweets, args.max_tweets)
    stream = tweepy.Stream(auth=auth, listener=testListener, timeout=args.timeout*60)

    print "Collecting tweets..."
    stream.filter(track=args.keywords)

    for twt in tweets:
        twt.disp()
        print

if __name__ == '__main__':
    main()


