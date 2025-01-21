from tkinter import *

# window configurations
window = Tk()
window.title("White Board")
window.configure(bg='#f2f3f5')
window.geometry('1050x570+150+50')
window.resizable(False, False)

# window icon
icon_image = PhotoImage(file='images/openfile.png')
window.iconphoto(True, icon_image)

color_box = PhotoImage(file="images/color.png")
label_ = Label(window, image=color_box, bg='#f2f3f5').place(x=10, y=20)


# eraser button
eraser_photo = PhotoImage(file='images/1eraser.png')
eraser_button = Button(window, image=eraser_photo).place(x=32, y=380)


# colors label canva
colors = Canvas(window, width=37, height=300 , bg='#ffffff', bd=0)
colors.place(x=30, y=60)


# drawing canva part
canvas = Canvas(window, width=930, height=500, background='white', cursor='hand2')
canvas.place(x=100, y=10)



window.mainloop()
