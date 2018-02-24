import parser
import ConfigParser

CONFIG="configuration/keys.ini"
def main():
    args = parser.get_args()
    config = ConfigParser.ConfigParser()

    # Config 
    config.read(CONFIG)
    config.get("keys", "ConsumerKey")
    config.get("keys", "ConsumerSecret")
    config.get("keys", "AccessToken")
    config.get("keys", "AccessSecret")

if __name__ == '__main__':
    main()


