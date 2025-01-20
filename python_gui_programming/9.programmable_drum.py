from tkinter import *


class DrumMachine():
    MAX_DRUM_NUM = 5

    def app(self):
        self.window = Tk()
        self.window.geometry('500x250')
        self.window.resizable(0,0)
        self.crate_top_bar()
        self.create_left_bar()
        self.crate_right_bar()
        self.create_play_bar()
        self.window.mainloop()


    def crate_top_bar(self):
        # create the main top frame
        top_bar_frame = Frame(self.window)
        top_bar_frame.grid(row=0,column=0, columnspan=12, rowspan=10, padx=5,pady=5,sticky=E+S+N+W)

        # units label added in top bar frame
        label = Label(top_bar_frame, text="Units:").grid(row=0, column=4)

        # creating a widget specific variable
        self.units = IntVar()
        self.units.set(4)

        # bpu widget spinbox
        self.bpu_widget = Spinbox(top_bar_frame, from_=0, to=10, width=5, textvariable=self.units, command=self.crate_right_bar)
        self.bpu_widget.grid(row=0, column=5)
        labell = Label(top_bar_frame, text='            ').grid(row=0 , column=6)

        # Bpu's label 
        bpu_lbl = Label(top_bar_frame, text='BPUs:').grid(row=0, column=7)
        self.bpu = IntVar()
        self.bpu.set(4)

        # creating unit's widget
        self.units_widget = Spinbox(top_bar_frame, width=5, textvariable=self.bpu, from_=1, to=8,command=self.crate_right_bar).grid(row=0, column=8)


    def create_left_bar(self):
        left_frame = Frame(self.window)
        left_frame.grid(row=10, column=0,
        columnspan=6, sticky=W+E+N+S)

        tbicon = PhotoImage(file='images/oopenfile.gif')
        for i in range(10, 15):
            button = Button(left_frame, image=tbicon)
            button.image = tbicon
            button.grid(row=i, column=0, padx=5, pady=2)
            self.drum_entry = Entry(left_frame)
            self.drum_entry.grid(row=i, column=4, padx=7, pady=2)
    

    def crate_right_bar(self):
        bpu = self.bpu.get()
        units = self.units.get()
        c = bpu * units
        right_frame = Frame(self.window)
        right_frame.grid(row=10, column=6,sticky=W+E+N+S, padx=15,pady=2)


        self.button = [[0 for x in range(c)] for x in range(self.MAX_DRUM_NUM)]
        for i in range(self.MAX_DRUM_NUM):

            for j in range(c):
                color = 'grey55' if (j / bpu) % 2 else 'khaki'
                self.button[i][j] = Button(right_frame, bg=color,
                width=1, command=self.button_clicked(i,j,bpu))
                self.button[i][j].grid(row=i, column=j)


    def button_clicked(self,i,j,bpu):
        def callback():
            btn = self.button[i][j]
            color = 'grey55' if (j/bpu)%2 else 'khaki'
            new_color = 'green' if btn.cget('bg') != 'green' else color
            btn.config(bg=new_color)
            return callback

        
    def create_play_bar(self):
        playbar_frame = Frame(self.window, height=15)
        ln = 15
        playbar_frame.grid(row=ln, columnspan=13, sticky=W+E, padx=15,pady=10)
        button = Button( playbar_frame, text ='Play')
        button.grid(row= ln, column=1, padx=1)
        button = Button( playbar_frame, text ='Stop')
        button.grid(row= ln, column=3, padx=1)


        loop = BooleanVar()
        loopbutton = Checkbutton(playbar_frame, text='Loop', variable=loop)
        loopbutton.grid(row=ln, column=16, padx=1)



if __name__ == '__main__':
    drum_sample = DrumMachine()
    drum_sample.app()        