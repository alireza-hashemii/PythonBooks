from tkinter import *

window = Tk()
window.geometry('400x170')



prior_name_label = Label(window, text='Name:').grid(row=0, column=0, sticky='e') 
replace_label = Label(window, text='Replace:').grid(row=1, column=0, sticky='e') 

entry_no1 = Entry(window)
entry_no2 = Entry(window)

entry_no1.grid(row=0, column=1,columnspan=9,sticky='we')
entry_no2.grid(row=1,column=1,sticky='we',columnspan=9)


btn1 = Button(window, text='Find',padx=20).grid(row=0 , column=10,sticky='ew')
btn2 = Button(window, text='Find All',padx=20).grid(row=1 , column=10,sticky=EW)
btn3 = Button(window, text='Replace',padx=20).grid(row= 2, column=10,sticky=EW)
btn4 = Button(window, text='Replace All',padx=20).grid(row=3 , column=10,sticky=EW)


Checkbutton(window, text='Match whole word only').grid(row =2, column=1, sticky='w')
Checkbutton(window, text='Match Case').grid(row =3, column=1,sticky='w')
Checkbutton(window, text='Wrap around').grid(row =4, column=1,sticky='w')

Radiobutton(window, text='Up', value=1).grid(row=3, column=6,sticky='w')
Radiobutton(window, text='Down', value=2).grid(row=3, column=7, sticky='e')



window.mainloop()


