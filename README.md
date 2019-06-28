# Sentiment Analysis of Facebook Comments #

Program was written in Python version 3.x, uses Library NLTK.


The project contribute serveral functionalities as listed below:

* Main.py - You can input any sentence, then program will use Library NLTK to analysis your sentence, and then it returns result that is how many percent of positive, negative or neutral.

* facebookComments.py - This is a part which will show you a Dashboard, which describes temporal sentiment analysis of comments on a post on Facebook. Data is got once, and then it will be analyzed in a processing.
You have to learn about Facebook Graph API and how it works. So, then paste your token and id of post in file "facebookComments.py", which you want to analysis sentiment of comments. Program will show you temporal sentiment analysis of comments.

* facebook_real_time.py - Our Real-time stream processing automates getting data from Facebook server continually and then, we process data in small time period – near real time. For every processing, we use NLTK Library to analysis sentiment data. The results of data processing will be checked by predefined user’s conditions. If it satisfies conditions, the program will create an event to update Dashboard’s status. Beside, the program includes a procedure, which implements listening to any event. If a certain events exists, Dashboard will be updated.

* A Method Automation Forecasting based on Cluster Profiles - For sentiment analysis of Facebook comment.ipynb  - Perfomance method to prediction the trend of development of people's attitude on a post.

### Architecture ###
Sentiment analysis sample:

<img src="https://raw.githubusercontent.com/saodem74/Sentiment-Analysis/master/pic/sentiment_analysis.png" alt="alt text" width="400" height="300">


Real time processing architecuture is described as below:

<img src="https://raw.githubusercontent.com/saodem74/Sentiment-Analysis/master/pic/system_realtime.png" alt="alt text" width="400" height="300">


Realtime processing sample:

<img src="https://raw.githubusercontent.com/saodem74/Sentiment-Analysis/master/pic/real_time_sample.png" alt="alt text" width="500" height="300">


Prdection sentiment of comment sample:

<img src="https://raw.githubusercontent.com/saodem74/Sentiment-Analysis/master/pic/prediction_sample.png" alt="alt text" width="600" height="250">

### Data Collection ###

Implementation of batch data processing makes sense in the case of high volumes data. Firstly, we chose a topic, which is popular recently. For each post, using Facebook Graph API, all comments have been collected during the first 30000 s. Data is stored in flat table format (e.g. CSV file) which is easy to save in distributed file system. The header of CSV file contains the following columns: [Datetime] [Topic] [Post] [Comment] [Positive] [Negative]. [Link data](https://raw.githubusercontent.com/saodem74/Sentiment-Analysis/master/Data/comment_data.csv)

The topic was chosen is “United States presidential election 2016”, which is popular recently. Almost data will be received from two famous new channels : BBC news and CNN on Facebook.

### Requirements ###

The project requires installed packages: 
* NLTK - Natural Language Toolkit is a leading platform for building Python programs to work with human language data
* facebook-sdk - Python SDK for Facebook's Graph API 
* matplotlib - Matplotlib is a Python 2D plotting library
* scikit-learn - Machine Learning library in Python
* pandas - an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming

### What is Sentiment Analysis? ###

   Sentiment Analysis is the process of determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker. A common use case for this technology is to discover how people feel about a particular topic.

### What is this NLTK? ###

* NLTK - Natural Language Toolkit is a leading platform for building Python programs to work with human language data
* Version: NLTK 3.1 released : October 2015
* [Link NLTK](http://www.nltk.org/)

### What is Facebook Graph API? ###
* The Graph API is the primary way for apps to read and write to the Facebook social graph
* [Link Facebook Graph API](https://developers.facebook.com/docs/graph-api)

### Publication ###
This project is publised on the International Conference as below:

Tran H., Shcherbakov M. (2016) Detection and Prediction of Users Attitude Based on Real-Time and Batch Sentiment Analysis of Facebook Comments. In: Nguyen H., Snasel V. (eds) Computational Social Networks. CSoNet 2016. Lecture Notes in Computer Science, vol 9795. Springer, Cham
[(Link Paper 1)](https://link.springer.com/chapter/10.1007/978-3-319-42345-6_24)
[(Link Paper 2)](https://arxiv.org/abs/1906.03392)

### Contributors ###

* Hieu Tran (trantrunghieu7492@gmail.com)


