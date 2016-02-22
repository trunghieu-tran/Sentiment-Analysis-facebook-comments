import csv
from pylab import *

xx = []
yPos = []
yNeg = []
fi_Pos = plt.figure()
fi_Neg = plt.figure()
fi = plt.figure()

cnt = 0
def drawAnnotate():

    plt.xlabel('Time(s)')
    plt.ylabel('Sentiment analysis')

def drawGraph(last):
    print(last)
    print(len(xx))
    ax1 = fi_Pos.add_subplot(111)
    axx1 = fi.add_subplot(111)
    ax2 = fi_Neg.add_subplot(111)
    axx2 = fi.add_subplot(111)

    ax1.plot(xx, yPos, color = 'g')
    axx1.plot(xx, yPos, color = 'g')
    ax2.plot(xx, yNeg, color = 'r')
    axx2.plot(xx, yNeg, color = 'r')
    xx.clear()
    yPos.clear()
    yNeg.clear()

def read_data_from_CSV_file():
    with open('Data/comment_data.csv','r',encoding='utf-8', errors='ignore') as csv_file:
        reader = csv.reader(csv_file, lineterminator='', delimiter=',')
        last = 'Post'
        for row in reader:
            if row[2] != last:
                if last != 'Post':
                    drawGraph(last)
                last = row[2]
                xx.append(row[0])
                yPos.append(row[4])
                yNeg.append(row[5])
            else:
                if last != 'Post':
                    xx.append(row[0])
                    yPos.append(row[4])
                    yNeg.append(row[5])
    drawAnnotate()
    show()
read_data_from_CSV_file()