# Twitter Writes The News

## Purpose
A facetious application that will generate (hopefully) hilarious articles from recent tweets.

Developed during HackIllinois 2018.

## Details
* User inputs keyword
* Application uses real-time tweets to create a paragraph news story based off of tweets related to the keyword
	* Real-time tweet REST API used (tweepy)
* Uses Markov chain to generate headline and article text
* Run locally (terminal)
* Developed in Python 2

## Setup and Install
1) Clone the repository:

```
git clone https://github.com/jerr-chen/twitter-writes-the-news.git``
pip install -r requirements.txt
```

3) Simple command to run the application with `keyword = "lol"`, `max_tweets = 100`, and `timeout = 1 minute`

```
python src/main.py --keyword lol --max_tweets 100 --timeout 1
```
