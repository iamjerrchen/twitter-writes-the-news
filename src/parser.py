import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Configures "Twitter Writes the News" with parameters.')

    parser.add_argument("--max_tweets", metavar='N', type=int, dest="max_tweets", default=500, help="The max tweets to collect for article construction.")
    # timeout units = minutes
    parser.add_argument("--timout", metavar='T', type=int, dest="timeout", default=5, help="The specified time before ending tweet collection.")
    parser.add_argument("--keyword", dest="keyword", help="The keyword of collected tweets.")

    return parser

def get_args():
    return get_parser().parse_args()
