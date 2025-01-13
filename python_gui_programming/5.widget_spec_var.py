from tkinter import *

# double - boolean - integer- string

window = Tk()
strr = StringVar()


label_1 = Label(window, text='Employee Number:').grid(row=0,column=0)
label_1 = Label(window, text='Employee Password:').grid(row=1,column=0)
entry = Entry(window, validate='key')
entry_2 = Entry(window, validate='focus',textvariable=strr)
Checkbutton(window, text='Remember Me').grid(row=2, column=1)
Button(window, text='Login').grid(row=2, column=5)


entry.grid(row=0, column=1, columnspan=5,sticky=EW,ipadx=30)
entry_2.grid(row=1, column=1, columnspan=5, sticky=EW)

window.mainloop()