# README #

This project is my Bachelor thesis about Sentiment Analysis.

Program was written in Python version 3.x, uses Library NLTK.

The content of the project is described below:

* 1st Program - Main.py - project SYS (show your sentiment)

You can input any sentence, then program will use Library NLTK to analysis your sentence, and then it returns result that is how many percent of positive, negative or neutral.

* 2nd Program - facebookComments.py - project TSAofCFB (temporal sentiment analysis of Facebook comments)

This is a part which will show you a Dashboard, which describes temporal sentiment analysis of comments on a post on Facebook. Data is got once, and then it will be analyzed in a processing.

* 3rd Program - facebook_real_time.py - project SART (Sentiment Analysis Real-time)

Our Real-time stream processing automates getting data from Facebook server continually and then, we process data in small time period – near real time. For every processing, we use NLTK Library to analysis sentiment data. The results of data processing will be checked by predefined user’s conditions. If it satisfies conditions, the program will create an event to update Dashboard’s status. Beside, the program includes a procedure, which implements listening to any event. If a certain events exists, Dashboard will be updated.


You have to learn about Facebook Graph API and how it works. So, then paste your token and id of post in file "facebookComments.py", which you want to analysis sentiment of comments. Program will show you temporal sentiment analysis of comments.

### What is Sentiment Analysis? ###

   Sentiment Analysis is the process of determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker. A common use case for this technology is to discover how people feel about a particular topic.

### What is this NLTK? ###

* NLTK - Natural Language Toolkit is a leading platform for building Python programs to work with human language data
* Version: NLTK 3.1 released : October 2015
* [Link NLTK](http://www.nltk.org/)

### What is Facebook Graph API? ###
* The Graph API is the primary way for apps to read and write to the Facebook social graph
* [Link Facebook Graph API](https://developers.facebook.com/docs/graph-api)

### Contributors ###

* Hieu Tran (trantrunghieu7492@gmail.com)
