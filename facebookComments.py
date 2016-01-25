import facebook
import dateutil.parser as dateparser
from pylab import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#  here is token which you get from Facebook Graph APIs
token = "CAACEdEose0cBALGIZASDgIrjQx9LSbv5dP7LNaZCCSHWfK2subPOlveBbpCKBHg5NpSzmKjPWe1WnqPJAysDMyvU6FDTRrgSYdX8Xb1R7A7XDMsgsZAZCOHUZCH2RS3YnuAljK7P3D1UYGHg2jDpvEGWz4XUJQ6ZCeBZAHOHDRKBoz6a8o9KaMXLGcY3R9ljdhrDqHQMwpvLre2vR9nJUOyw49nultxXSMZD"
graph = facebook.GraphAPI(token)
post_ids = ['4692106117913_10201248719057316'] # here is a array of post_ids
posts = graph.get_objects(ids=post_ids)

# Function get all coments from id-post
def getComments(id_post):
    sentencesComments = []
    timeComments = []
    comments = graph.get_connections(id=id_post, connection_name='comments', limit = 200 )
    cnt = 0
    for comment in comments['data']:
        try:
            cnt = cnt + 1
            print('Comment {0} : {1} -- Time = {2}'.format(cnt, comment['message'], comment['created_time']))
            sentencesComments.append(comment['message'])
            timeComments.append(comment['created_time'])
        except:
            continue
    return sentencesComments, timeComments

# Convert time comment to coordinate X in Graph
def timeToX(timeComments, created_time_post):
    timeX = []
    for timeComment in timeComments:
        distTime = dateparser.parse(timeComment) - created_time_post
        x = int(distTime.total_seconds())
        timeX.append(x)
    return timeX

#  Sentiment Analysis comment using NLTK library
def sentimentAnalysis(sentencesComments):
    posY = []
    negY = []
    sid = SentimentIntensityAnalyzer()
    sumPos = 0
    sumNeg = 0
    cnt = 0
    for sentence in sentencesComments:
        cnt += 1
        ss = sid.polarity_scores(sentence)
        for type in sorted(ss):
            if (type == "neg"):
                sumNeg += ss[type]
                negY.append(sumNeg / cnt)
            if (type == "pos"):
                sumPos += ss[type]
                posY.append(sumPos / cnt)
    return posY, negY

# For each Id_post, we run analysis and create graph temporal sentiment analysis of comments facebook
for post_id in post_ids:
    created_time_post = dateparser.parse(posts[post_id]['created_time'])
    print('Created Time of Post = {0}'.format(created_time_post))
    sentencesComments, timeComments = getComments(post_id)
    timeX = timeToX(timeComments, created_time_post)
    posY, negY = sentimentAnalysis(sentencesComments)
    # plt.scatter(timeX, posY) - it will show exactly points if you need
    # plt.scatter(timeX, negY)
    fig1 = plt.plot(timeX, posY, color = 'g')
    fig2 = plt.plot(timeX, negY, color = 'r')

    posYannotate = 20 if posY[0] < 0.5 else -20
    negYannotate = 20 if negY[0] < 0.5 else -20
    plt.annotate('Positive', xy=(timeX[0], posY[0]), xytext=(40,posYannotate),
                    textcoords='offset points', ha='center', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',
                                    color='blue'))
    plt.annotate('Negative', xy=(timeX[0], negY[0]), xytext=(40,negYannotate),
                    textcoords='offset points', ha='center', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',
                                    color='blue'))

    show()