import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Configures "Twitter Writes the News" with parameters.')

    parser.add_argument("--max_tweets", type=int, dest="max_tweets", default=100, help="The max tweets to collect for article construction.")
    # timeout units = minutes
    parser.add_argument("--timeout", type=int, dest="timeout", default=2, help="The specified time in minutes before ending tweet collection.")
    parser.add_argument("--keywords", "--keyword", dest="keywords", nargs="+", help="The keyword of collected tweets.")
    parser.add_argument("--state_size", type=int, dest="state_size", default=4, help="The number of continuous words for markov chain.")
    parser.add_argument("--max_words", type=int, dest="max_words", default=100, help="The maximum number of words in the generated text.")

    return parser

def get_args():
    return get_parser().parse_args()
