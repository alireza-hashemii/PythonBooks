from tkinter import *

# four args of pack geometry manager(side - fill - anchor - expand)


window = Tk()
window.geometry('400x350')

def a_clicked():
    if btB['state'] == DISABLED:
        btB['state'] = ACTIVE
    else:
        btB['state'] = DISABLED


btA = Button(window, text='A',bg='lime',width=15,command=a_clicked).pack(side=LEFT, fill=Y)
btB = Button(window, text='B',bg='purple',height=2)
btC = Button(window, text='C',bg='lightblue',height=3).pack(side=TOP, fill=X)
btD = Button(window, text='D',bg='orange',height=4).pack(side=BOTTOM, fill=X)
btE = Button(window, text='E',bg='pink').pack(side=LEFT, fill=BOTH,expand=True)

btB.pack(side=TOP,fill=X)
window.mainloop()