from tkinter import *
import facebook
import dateutil.parser as dateparser
from pylab import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

##### Connections to Facebook by Graph API
#  here is token which you get from Facebook Graph APIs, every time using program, you need update this token
token = "CAACEdEose0cBALUEDgnZAmcJPdeVuJFfuah5atvisexHnd9eNEeY2vrqLD2gOZCL947p6AdfVUYuWJ2SUl92a57kF57atouwENILbqJRFesNZCjytWSQIPhEo2XvAttpzmvFdjglaUpQFCKcHdsXZAujHnsGvcYZCIsWHRSL4ipmFPkQKCmNYHgbHsPTDPEKZCilvxy2qlyZCkndAZCfgmBPDhmIyPtV7dwZD"
graph = facebook.GraphAPI(token)
# here is a array of post_ids
# CNN : 5550296508
# BBC : 1143803202301544
# my  : 4692106117913
# CNNpolitics : 219367258105115
post_ids = [
            '1143803202301544_10153388347607217'
           ]
currPost = "National poll: Sanders and Clinton neck-and-neck"
posts = graph.get_objects(ids=post_ids)
############
xx = []
yyPos = []
yyNeg = []

# Function get all coments from id-post
def getComments(id_post):
    sentencesComments = []
    timeComments = []
    comments = graph.get_connections(id=id_post, connection_name='comments', limit = 1000)
    cnt = 0
    for comment in comments['data']:
        try:
            cnt = cnt + 1
            # print('Comment {0} : {1} -- Time = {2}'.format(cnt, comment['message'], comment['created_time']))
            sentencesComments.append(comment['message'])
            timeComments.append(comment['created_time'])
        except:
            continue
    return sentencesComments, timeComments


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

# Convert time comment to coordinate X in Graph
def timeToX(timeComments, created_time_post):
    timeX = []
    for timeComment in timeComments:
        distTime = dateparser.parse(timeComment) - created_time_post
        x = int(distTime.total_seconds())
        timeX.append(x)
    return timeX

def satisfyConditions(sentencesCommentsCurr, sentencesComments):
    res = len(sentencesCommentsCurr) > len(sentencesComments)
    return res

class Observer():
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observed_events = []
    def observe(self, event_name, callback_fn):
        self._observed_events.append({'event_name' : event_name, 'callback_fn' : callback_fn})


class Event():
    def __init__(self, event_name, *callback_args):
        for observer in Observer._observers:
            for observable in observer._observed_events:
                if observable['event_name'] == event_name:
                    observable['callback_fn'](*callback_args)

def drawAnnotate():
    plt.xlabel('Time(s)')
    plt.ylabel('Sentiment analysis')

stop = False
def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        global stop
        stop = True

class drawgraph(Observer):
    def __init__(self):
        Observer.__init__(self) # DON'T FORGET THIS
    def new_point(self, x, y, y2):
        # plt.scatter(x, y)
        xx.append(x)
        yyPos.append(y)
        yyNeg.append(y2)
        plt.plot(xx, yyPos, color = 'g')
        plt.plot(xx, yyNeg, color = 'r')
        drawAnnotate()
        plt.show()
        # plt.pause(0.001) #Note this correction



def main_real_time_analysis():
    # create observation
    dr = drawgraph()
    dr.observe('draw a new point',  dr.new_point)
    # create graph real-time
    plt.ion()
    fig=plt.figure()
    # listen keyboard to exit
    fig.canvas.mpl_connect('key_press_event', press)

    #### Draw graph for data which have existed
    # Get created time of post
    created_time_post = dateparser.parse(posts[post_ids[0]]['created_time'])
    print('Created Time of Post = {0}'.format(created_time_post))
    # Get comment of post
    sentencesComments, timeComments = getComments(post_ids[0])
    # Convert time data
    timeX = timeToX(timeComments, created_time_post)
    # Convert sentiment analysis data
    posY, negY = sentimentAnalysis(sentencesComments)
    for i in range(len(posY) - 1):
        Event('draw a new point', timeX[i], posY[i], negY[i])
    plt.plot(xx, yyPos, color = 'g')
    plt.plot(xx, yyNeg, color = 'r')
    drawAnnotate()
    plt.show()
    #############
    ############# Real-time graph ####
    # Real-time
    while stop == False:
        sentencesCommentsCurr, timeCommentsCurr = getComments(post_ids[0])
        if satisfyConditions(timeCommentsCurr, timeComments):
            timeXCurr = timeToX(timeCommentsCurr, created_time_post)
            posYCurr, negYCurr = sentimentAnalysis(sentencesCommentsCurr)
            for i in range(len(sentencesComments), len(sentencesCommentsCurr)):
                Event('draw a new point', timeXCurr[i], posYCurr[i], negYCurr[i])
            print("updated {0} comments".format(len(sentencesCommentsCurr) - len(sentencesComments)))
            sentencesComments = sentencesCommentsCurr
            timeComments = timeCommentsCurr
            timeX = timeXCurr
        plt.pause(0.1)

    print("Done")

def isEnglishLanguage(str):
    for char in str:
        i = ord(char)
        if i < 0 or i > 255:
            return False
    return True

def isValid(str):
    res = not ("http://" in str)
    res = res and  not("https://" in str)
    return res

def isInTimeLimit(t):
    return t < 30000

def write_data_to_CSV_file():
    import csv
    topic = "United States presidential election 2016"
    # option 'w' - create a new file
    # option 'a' - append rows to the old file
    with open('comment_data.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n', delimiter=',')
        # Header
        # writer.writerow(['DateTime(seconds)', 'Topic', 'Post', 'Comment', 'Positive', 'Negative'])
        created_time_post = dateparser.parse(posts[post_ids[0]]['created_time'])
        sentencesComments, timeComments = getComments(post_ids[0])
        timeX = timeToX(timeComments, created_time_post)
        posY, negY = sentimentAnalysis(sentencesComments)
        for i in range(len(timeX)):
            if isEnglishLanguage(sentencesComments[i]) and isValid(sentencesComments[i]) and isInTimeLimit(timeX[i]):
                writer.writerow([timeX[i], topic, currPost, sentencesComments[i], posY[i], negY[i]])


# main_real_time_analysis()
# write_data_to_CSV_file()