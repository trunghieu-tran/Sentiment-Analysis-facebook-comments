from tkinter import *
import tkinter.messagebox

# Main function in program
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def callback():
    if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        main.destroy()

def runAnalysis():
    typedText.configure(text = "Your text: " + line.get())

# Create main window
main = Tk()
main.title("Sentiment Analysis")
main.geometry("500x300")
main.resizable(width=FALSE, height=FALSE)
main.protocol("WM_DELETE_WINDOW", callback)
main.focus()
center(main)

# addition item on window
label1 = Label(text = "Type your review:")
label1.pack()

def typeKeyReturn(event):
    runAnalysis()

line = Entry(main, width=70)
line.bind("<Return>",typeKeyReturn)
line.bind("<Key>",typeKeyReturn)
line.pack()

typedText = Label(text = "Your text :")
typedText.pack()

analysisButton = Button(main, text = "Analysis", width=10, command = runAnalysis)
analysisButton.grid(row=50, column=550)
analysisButton.pack()



# Run program
mainloop()