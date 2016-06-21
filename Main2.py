from tkinter import *
import tkinter.messagebox

from nltk.sentiment.vader import SentimentIntensityAnalyzer

class analysis_text():
        # Main function in program
    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def callback(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            self.main.destroy()

    def setResult(self, type, res):
        if (type == "neg"):
            self.negativeLabel.configure(text = "Отрицательно : " + str(res) + " % \n")
        if (type == "neu"):
            self.neutralLabel.configure( text = "Нейтрально : " + str(res) + " % \n")
        if (type == "pos"):
            self.positiveLabel.configure(text = "Положительно : " + str(res) + " % \n")

    def runAnalysis(self):
        sentences = []
        sentences.append(self.line.get())
        sid = SentimentIntensityAnalyzer()
        for sentence in sentences:
            # print(sentence)
            ss = sid.polarity_scores(sentence)
            for k in sorted(ss):
                self.setResult(k, ss[k])
                    # print('{0}: {1} \n'.format(k, ss[k]), end='')
        print()

    def editedText(self, event):
        self.typedText.configure(text = self.line.get() + event.char)

    def runByEnter(self, event):
        self.runAnalysis()

    def __init__(self):
        # Create main window
        self.main = Tk()
        self.main.title("Анализ тональности")
        self.main.geometry("500x300")
        self.main.resizable(width=FALSE, height=FALSE)
        self.main.protocol("WM_DELETE_WINDOW", self.callback)
        self.main.focus()
        self.center(self.main)

        # addition item on window
        self.label1 = Label(text = "Ввод текста:")
        self.label1.pack()

        # Add a hidden button Enter
        self.line = Entry(self.main, width=70)
        self.line.pack()

        self.textLabel = Label(text = "\nВведенные тексты:", font=("Helvetica", 15))
        self.textLabel.pack()
        self.typedText = Label(text = "", fg = "blue", font=("Helvetica", 20))
        self.typedText.pack()

        self.line.bind("<Key>",self.editedText)
        self.line.bind("<Return>",self.runByEnter)


        self.result = Label(text = "\nРезультаты", font=("Helvetica", 15))
        self.result.pack()
        self.negativeLabel = Label(text = "", fg = "red", font=("Helvetica", 20))
        self.negativeLabel.pack()
        self.neutralLabel  = Label(text = "", font=("Helvetica", 20))
        self.neutralLabel.pack()
        self.positiveLabel = Label(text = "", fg = "green", font=("Helvetica", 20))
        self.positiveLabel.pack()
        # Run program


myanalysis = analysis_text()
# myanalysis.setResult("neg", 0.5)
# print(myanalysis.negativeLabel.cget("text"))
mainloop()
