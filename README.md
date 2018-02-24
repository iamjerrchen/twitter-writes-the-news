# Twitter Writes The News

## Purpose
A facetious application that will generate (hopefully) hilarious articles from recent tweets.

Developed during HackIllinois 2018.

## Brainstorm
* User inputs keyword
* Application uses real-time tweets to create a headline and story based off of the tweets
	* Real-time tweet API used
* Hosted locally
* Developed in Python 2

### Module Explanation
#### main
* Top level module to run the program

#### twitter
* Module that makes the POST calls to twitter and returns the JSON data

#### tweet
* Module that represents a single tweet

#### article
* Module that constructs the article

## Future Ideas
* Implement a web client
* Save articles
* Search through previously saved articles 
