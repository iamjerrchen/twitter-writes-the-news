import parser
import ConfigParser
import twitter

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
    api = twitter.Api(consumer_key, consumer_secret, access_token, access_secret)
    print api.VerifyCredentials()

    # Sample code that gets and prints stream
    stream = api.GetStreamFilter(track=["hello"])
    while True:
    	for tweet in stream:
    		print (tweet)

if __name__ == '__main__':
    main()


