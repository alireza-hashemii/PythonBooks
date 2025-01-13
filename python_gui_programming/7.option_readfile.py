from tkinter import *

window = Tk()
window.option_readfile('optionDB.txt')


Label(window,text='AAAA').pack()
btn_1 = Button(window, text='UNO').pack()
btn_2 = Button(window, text='DOS').pack()
btn_3 = Button(window, text='TRES').pack() 

# removing the border without frame (unmovable and unresizeable)
# window.overrideredirect(TRUE)

window.mainloop()