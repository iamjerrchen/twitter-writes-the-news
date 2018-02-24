# Twitter Writes The News

## Purpose
A facetious application that will generate (hopefully) hilarious articles from recent tweets.

Under development during HackIllinois 2018.

## Details
* User inputs keyword
* Application uses real-time tweets to create a headline and story based off of tweets related to the keyword
	* Real-time tweet REST API used (tweepy)
* Uses Markov chains to generate headline and article text
* Hosted locally (terminal)
* Developed in Python 2

## Setup and Install
Get the required packages:
	`pip install -r requirements.txt`

You need to install these within nltk:
	```python -i
	import nltk
	nltk.download('stopwords')
	exit()
	```



### Module Explanation
#### main
* Top level module to run the program

#### tweet
* Module that represents a single tweet

#### article
* Module that constructs the article

#### parser
* Parses arguments from the user input in the terminal when running the application

#### stream_listener
* Uses Tweepy to collect a stream of tweets based on user parameters

## Future Ideas
* Implement a web client
* Save articles
* Search through previously saved articles 
