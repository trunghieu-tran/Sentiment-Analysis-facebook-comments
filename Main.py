from tkinter import *

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


main = Tk()
main.title("Sentiment Analysis")
main.geometry("500x300")
main.resizable(width=FALSE, height=FALSE)
center(main)

label1 = Label(text = "Type your review:")
label1.pack()

line = Entry(main, width=70)
line.pack()

def runAnalysis():
    print("hello cac ban")

analysisButton = Button(main, text = "Analysis", width=10, command = runAnalysis)
analysisButton.grid(row=50, column=550)
analysisButton.pack()


w = Canvas(main, width=200, height=100)
w.pack()

# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
# w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()