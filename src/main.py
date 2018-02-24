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

    # Testing stream listener
    tweets = []
    testListener = stream_listener(tweets, 10)
    stream = tweepy.Stream(auth=auth, listener=testListener, timeout=30)

    stream.filter(track=["donald trump"])

    for twt in tweets:
        twt.disp()
        print

if __name__ == '__main__':
    main()


