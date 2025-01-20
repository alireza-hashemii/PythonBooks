from tkinter import *

win = Tk()
win.geometry('500x400')

frame_top = Frame(win, height=100,width=500, bg='lime').grid(row=0,column=0, columnspan=10, rowspan=4, sticky=W+S+E+N)
left_frame = Frame(win,height=300, width=50, bg='gold' ).grid(row=4, column=0, columnspan=4,rowspan=6,sticky=W+S+E+N)
# for i in range(4):
#     Button(left_frame,text="A").grid(row=4+i,column=0)
#     entry = Entry(left_frame)
#     entry.grid(row=4+i , column=3)
Spinbox(left_frame, from_=0,to=2).grid(row=2,column=2)
win.mainloop()