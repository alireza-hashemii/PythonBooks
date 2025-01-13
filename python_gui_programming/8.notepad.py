from tkinter import *

# accelerator - compound - underline

# Basic configuration of window
window = Tk()
window.geometry('450x350')
window.title("Notepad")



# basic functionality 
def cut():
    textPad.event_generate("<<Cut>>")

def copy():
    textPad.event_generate("<<Copy>>")

def paste():
    textPad.event_generate("<<Paste>>")

def undo():
    textPad.event_generate('<<Undo>>')

def redo():
    textPad.event_generate("<<Redo>>")


def redo():
    textPad.event_generate("<<SelectAll>>")

def on_find():
    global t2
    t2 = Toplevel(window)
    t2.title('Find')
    t2.geometry('262x65+200+250')
    t2.transient(window)

    Label(t2, text="Find All:").grid(row=0, column=0, sticky='e')
    v=StringVar()
    e = Entry(t2, width=25, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    e.focus_set()
    c=IntVar()
    Checkbutton(t2, text='Ignore Case', variable=c).grid(row=1,
    column=1, sticky='e', padx=2, pady=2)
    Button(t2, text="Find All", underline=0, command=lambda:
    search_for(v.get(), c.get(), textPad, t2, e)).grid(row=0,
    column=2, sticky='e'+'w', padx=2, pady=2)
    

def search_for(needle, cssnstv, textPad, t2, e) :
    textPad.tag_remove('match', '1.0', END)
    count =0
    if needle:
        pos = '1.0'
    while True:
        pos = textPad.search(needle, pos, nocase=cssnstv,
        stopindex=END)

        if not pos:
            break
        else:
            lastpos = '%s+%dc' % (pos, len(needle))
            print(len(needle), pos, lastpos)
            textPad.tag_add('match', pos, lastpos)
            count += 1
            pos = lastpos
            textPad.tag_config('match', foreground='red',
            background='yellow')
            e.focus_set()
            t2.title('%d matches found' %count)
            t2.protocol("WM_DELETE_WINDOW", close_search)

def close_search():
    textPad.tag_remove('match', '1.0', END)
    t2.destroy()
# Main top menu
menubar = Menu(window)

# first option and it's child options
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Open", )
filemenu.add_command(label="New",)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label='File', menu=filemenu)


# second menu option and it's child options
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo",accelerator='Ctrl+Z',command=undo)
editmenu.add_command(label="Redo",accelerator='Ctrl+Y', command=redo )
editmenu.add_separator()
editmenu.add_command(label="Copy", accelerator='Ctrl+C',underline=0,command=copy) 
editmenu.add_command(label="Select All", accelerator='Ctrl+A') 
editmenu.add_command(label="Paste",accelerator='Ctrl+V',command=paste)
editmenu.add_command(label="Cut",accelerator='Ctrl+X', command=cut)

menubar.add_cascade(label='Edit', menu=editmenu)



# Third menu option
viewmenu = Menu(menubar, tearoff=0)
window.config(menu=menubar)
viewmenu.add_command(label="Minimize")
viewmenu.add_command(label="Maximize")
viewmenu.add_command(label="Find", command=on_find)
viewmenu.add_command(label="Delete Borders",) 
viewmenu.add_checkbutton(label='Show Line Number', variable=viewmenu)
themesmenu = Menu(viewmenu)
# Needs change in future updates.
themesmenu.add_radiobutton(label="Bright as Day", variable=themesmenu)
themesmenu.add_radiobutton(label="Dark as Night", variable=themesmenu)
themesmenu.add_radiobutton(label="Green as Meadow", variable=themesmenu)

viewmenu.add_cascade(label="Themes", menu=themesmenu)
menubar.add_cascade(label='View', menu=viewmenu)

themesmenu = Menu(viewmenu)

# 2 vertical and horizontal colored lines
shortcutbar = Frame(window, height=25, bg='light sea green')
shortcutbar.pack(expand=NO, fill=X)

lnlabel = Label(window, width=2, bg = 'antique white')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)



# text pad and scroll over it in vertical direction
textPad = Text(window,background='#e9f7ef',undo=True,font=('Comic Sans MS',12, 'bold'))
textPad.pack(fill=BOTH, expand=YES)


scroll= Scrollbar(textPad)
textPad.configure(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)





window.mainloop()