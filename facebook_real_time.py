from tkinter import *
import facebook
import dateutil.parser as dateparser
from pylab import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

##### Connections to Facebook by Graph API
#  here is token which you get from Facebook Graph APIs, every time using program, you need update this token
token = "EAACEdEose0cBAKz7x4gPKUseSB7tx3uJo3Ot79Ca1QHbkNmzIjgTaZAvjz2zHvHXZCRlr39CmrPQmvgwYVNzzkn7OMT9OhmbkImixZAIFkZAtaNNE9wGe9ZAoLZAZALSLWfkXfTZAYMVqVZBlFSnZCXwo2XmR5n7ZBmOhWTrZB8qXF3YZAQZDZD"
graph = None
# here is a array of post_ids
# CNN : 5550296508
# BBC : 1143803202301544
# BBC new : 228735667216
# my  : 4692106117913
# CNNpolitics : 219367258105115
post_ids = []
currPost = "NONE"
posts = None
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
                negY.append(sumNeg / cnt) # this is for run-realtime
                # negY.append(ss[type])  # this is for saving data to file CSV
            if (type == "pos"):
                sumPos += ss[type]
                posY.append(sumPos / cnt) # this is for run-realtim
                # posY.append(ss[type]) # this is for saveing data
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


def sortCommentbyTime(timeX, posY, negY):
    for i in range(len(timeX)):
        for j in range(i + 1, len(timeX)):
            if (timeX[i] > timeX[j]):
                timeX[i], timeX[j] = timeX[j], timeX[i]
                posY[i],  posY[j]  = posY[j],  posY[i]
                negY[i],  negY[j]  = negY[j],  negY[i]

def main_real_time_analysis():
    global posts, token, graph, post_ids
    # input token + id post
    # token = input("Input access token:")
    # idpost = input("Input post ID:")
    # idpage = input("Input page ID:")
    # idpost = '10201756757877969'
    token = sys.argv[1]
    idpost = sys.argv[2]
    idpage = sys.argv[3]
    post_ids.append(idpage + "_" + idpost)
    graph = facebook.GraphAPI(token)
    posts = graph.get_objects(ids=post_ids)

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
    # sort data
    sortCommentbyTime(timeX, posY, negY)

    lastMoment = 0
    for i in range(len(posY)):
        Event('draw a new point', timeX[i], posY[i], negY[i])
        # print("{0} {1} {2}".format(timeX[i], posY[i], negY[i]))
        lastMoment = timeX[i]

    plt.plot(xx, yyPos, color = 'g')
    plt.plot(xx, yyNeg, color = 'r')
    drawAnnotate()
    plt.show()
    #############
    ############# Real-time graph ####
    # Real-time
    while stop == False:
        sentencesCommentsCurr, timeCommentsCurr = getComments(post_ids[0])
        # if satisfyConditions(timeCommentsCurr, timeComments):
        # if (len(timeCommentsCurr) > len(timeX)):

        timeXCurr = timeToX(timeCommentsCurr, created_time_post)
        posYCurr, negYCurr = sentimentAnalysis(sentencesCommentsCurr)

        sortCommentbyTime(timeXCurr, posYCurr, negYCurr)

        cntUpdate = 0
        for i in range(len(sentencesCommentsCurr)):
            if (timeXCurr[i] >  lastMoment):
                cntUpdate += 1
                Event("draw a new point", timeXCurr[i], posYCurr[i], negYCurr[i])
                timeX.append(timeXCurr[i])
                # print(timeXCurr[i])
                lastMoment = timeXCurr[i]
        if (cntUpdate > 0):
            print("updated {0} comments".format(cntUpdate))

        # sentencesComments = sentencesCommentsCurr
        # timeComments = timeCommentsCurr
        # timeX = timeXCurr
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
    global posts
    posts = graph.get_objects(ids=post_ids)
    # option 'w' - create a new file
    # option 'a' - append rows to the old file
    with open('Data/comment_data_2.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n', delimiter=',')

        # Header - anable in the first time when you write into the file
        # writer.writerow(['DateTime(seconds)', 'Topic', 'Post', 'Comment', 'Positive', 'Negative'])
        created_time_post = dateparser.parse(posts[post_ids[0]]['created_time'])
        sentencesComments, timeComments = getComments(post_ids[0])
        timeX = timeToX(timeComments, created_time_post)
        posY, negY = sentimentAnalysis(sentencesComments)
        for i in range(len(timeX)):
            if isEnglishLanguage(sentencesComments[i]) and isValid(sentencesComments[i]) and isInTimeLimit(timeX[i]):
                writer.writerow([timeX[i], topic, currPost, sentencesComments[i], posY[i], negY[i]])


def from_link_to_get_comment(link):
    import csv
    global  currPost
    global  post_ids
    with open(link, 'r',encoding='utf-8', errors='ignore') as csv_file:
        reader = csv.reader(csv_file, lineterminator='', delimiter=',')
        cnt = 0
        for row in reader:
            cnt += 1
            print(cnt,  ' ', row)
            post_ids[0] = str(row[1])
            currPost = row[0]
            write_data_to_CSV_file()


# from_link_to_get_comment('Data/LinkPost.csv')
main_real_time_analysis()
# write_data_to_CSV_file()