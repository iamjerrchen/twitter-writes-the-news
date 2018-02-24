# Twitter Writes The News

## Purpose
A facetious application that will generate (hopefully) hilarious articles from recent tweets.

Developed during HackIllinois 2018.

## Details
* User inputs keyword
* Application uses real-time tweets to create a headline and story based off of tweets related to the keyword
	* Real-time tweet REST API used
* Hosted locally (terminal)
* Developed in Python 2

### Module Explanation
#### main
* Top level module to run the program

#### twitter
* Wrapper module that makes the POST calls to twitter and returns the JSON data

#### tweet
* Module that represents a single tweet

#### article
* Module that constructs the article

#### parser
* Parses arguments from the user input in the terminal when running the application

## Future Ideas
* Implement a web client
* Save articles
* Search through previously saved articles 
