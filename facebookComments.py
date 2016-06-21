import facebook
import dateutil.parser as dateparser
from pylab import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#  here is token which you get from Facebook Graph APIs, every time using program, you need update this token
token = "CAACEdEose0cBAAFjBydnbq2X405Al0bZCWW1cV9yFjZAMh9yYs7m3Jz4EiiZCVL0X8O9XLLsOhHLjCupxGARTniLlb0GBzFs9rT2maWo4pZBZBZAXhohZCzMI7XiaXghfrcRE7M5h0GUngTDLQXjw2hQMQ2Qz4mkZC3yEIr0krOpUGZBJKUg8OeUuggz0GkpZCzkcgGdLqheZBQBcelOdOfOGVujYNovGixBS0ZD"
graph = facebook.GraphAPI(token)
# here is a array of post_ids
# The 1st ID is BBC, the 2nd ID is CNN
post_ids = [
            '526077330801741_957234144352722'
            # '1143803202301544_10153361940712217',
            # '5550296508_10154411968366509'
           ]
post_titles = [
                'TSAofCFB on BBC for article: Obama bans solitary confinement for juveniles',
                'TSAofCFB on CNN for article: Obama bans solitary confinement for juveniles'
              ]
posts = graph.get_objects(ids=post_ids)

# Function get all coments from id-post
def getComments(id_post):
    sentencesComments = []
    timeComments = []
    comments = graph.get_connections(id=id_post, connection_name='comments', limit = 1000)
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
fi = [plt.figure()] * len(post_ids)
cnt = 0
for post_id in post_ids:
    # Get created time of post
    created_time_post = dateparser.parse(posts[post_id]['created_time'])
    print('Created Time of Post = {0}'.format(created_time_post))
    # Get comment of post
    sentencesComments, timeComments = getComments(post_id)
    # Convert time data
    timeX = timeToX(timeComments, created_time_post)
    # Convert sentiment analysis data
    posY, negY = sentimentAnalysis(sentencesComments)

    # plt.scatter(timeX, posY) #  it will show exactly points if you need
    # plt.scatter(timeX, negY)

    fi[cnt] = plt.figure()
    # fig1 = plt.plot(timeX, posY, color = 'g')
    # fig2 = plt.plot(timeX, negY, color = 'r')
    ax1 = fi[cnt].add_subplot(111)
    ax2 = fi[cnt].add_subplot(111)
    ax1.plot(timeX, posY, color = 'g')
    ax2.plot(timeX, negY, color = 'r')

    # Draw annotate of graph
    posYannotate = 20 if posY[0] < 0.5 else -20
    negYannotate = 20 if negY[0] < 0.5 else -20
    index = len(timeX)- 1
    plt.annotate('Positive', xy=(timeX[index], posY[index]), xytext=(40,posYannotate),
                    textcoords='offset points', ha='center', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',
                                    color='blue'))
    plt.annotate('Negative', xy=(timeX[index], negY[index]), xytext=(40,negYannotate),
                    textcoords='offset points', ha='center', va='bottom',
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',
                                    color='blue'))

    plt.xlabel('Time(s)')
    plt.ylabel('Sentiment analysis')
    fi[cnt].suptitle(post_titles[cnt])
    cnt += 1
# Show graph
show()