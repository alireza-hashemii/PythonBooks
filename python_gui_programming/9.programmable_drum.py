from tkinter import *
from tkinter import dialog
import os
import winsound

class DrumMachine():
    MAX_DRUM_NUM = 5
    def __init__(self):
       
        self.widget_drum_name = []
        self.widget_drum_file_name = [0] * self.MAX_DRUM_NUM
        self.current_drum_no = 0

    def app(self):
        self.window = Tk()
        self.window.geometry('500x250')
        self.window.resizable(0,0)
        self.crate_top_bar()
        self.create_left_bar()
        self.crate_right_bar()
        self.create_play_bar()
        self.play_audio('file1.ogg')
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
            button = Button(left_frame, image=tbicon,command=lambda: self.drum_load(i-10))
            button.image = tbicon
            button.command = self.drum_load(i - 10)
            button.grid(row=i, column=0, padx=5, pady=2)
            self.drum_entry = Entry(left_frame)
            self.drum_entry.grid(row=i, column=4, padx=7, pady=2)
            self.widget_drum_name.append(self.drum_entry)
    

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
            color = 'grey55' if (j/bpu) % 2 else 'khaki'
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


    def drum_load(self, drum_no):
        def callback():
            self.current_drum_no = drum_no
            try:
                file_name = dialog.askopenfilename(
                defaultextension=".wav", filetypes=[("Wave Files","*.wav"),("OGG Files","*.ogg")])
                if not file_name: 
                    return None
                try:
                    del self.widget_drum_file_name[drum_no]
                except: 
                    pass
                self.widget_drum_file_name.insert(drum_no, file_name)
                drum_name = os.path.basename(file_name)
                self.widget_drum_name[drum_no].delete(0, END)
                self.widget_drum_name[drum_no].insert(0, drum_name)
            except:
                dialog.showerror('Invalid', "Error loading drum samples")
            return callback
        


if __name__ == '__main__':
    winsound.PlaySound('file1.ogg',winsound.SND_FILENAME)
    drum_sample = DrumMachine()
    drum_sample.app()        