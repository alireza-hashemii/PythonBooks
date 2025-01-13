from tkinter import *
import time
from tkinter import ttk

# instance level - class level - application level - button.configure()
# Button.bind_all()
# Button.bind_class()

window = Tk()


def dstry_page(event):
    lbl = Label(window, text="WORKED")
    lbl.pack()


btn = ttk.Button(window,text="Hello")
btn.configure(cursor='cross')
btn.bind("<KeyPress-A>", dstry_page)# bind to keypress A
btn.pack()


window.mainloop()

