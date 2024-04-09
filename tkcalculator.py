from tkinter import *

root = Tk()

title = Label(root, text="calculator")
button1 = Button(root, text="1")
button2 = Button(root, text="2")
button3 = Button(root, text="3")


title.grid(row=0 , column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

root.mainloop()