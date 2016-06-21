from tkinter import *
import tkinter.messagebox
import os

text_width = 100

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

def Done():
    if tkinter.messagebox.askokcancel("Done", "Are you ready?"):
        cmd = "python3 facebook_real_time.py " + token.get() + " " + idpost.get() + " "  + idpage.get()
        main.destroy()
        os.system(cmd)


main = Tk()
main.title("Real-time Analysis")
main.resizable(width=FALSE, height=FALSE)
main.protocol("WM_DELETE_WINDOW", callback)
main.focus()

tokenLab = Label(text = "Token:")
tokenLab.pack()

token = Entry(main, width = text_width)
token.focus_set()
token.pack()

idpostLab = Label(text = "Post ID:")
idpostLab.pack()

idpost = Entry(main, width = text_width)
idpost.pack()

idpageLab = Label(text="Page ID:")
idpageLab.pack()
idpage = Entry(main, width = text_width)
idpage.pack()

b = Button(main, text = "Run", width = 10, command = Done)
b.pack()

center(main)
mainloop()