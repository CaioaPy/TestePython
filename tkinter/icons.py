from tkinter import *

root = Tk()
e = Entry(root, borderwidth=3)
e.pack()

def Regular_click():
    label = Label(root, text="You clicked a button.")
    label.pack()

def grab_click():
    label = Label(root,text=e.get())
    label.pack()

button1 = Button(root, text="The Button", command=Regular_click)
button2 = Button(root, text="The broken Button", state=DISABLED)
button3 = Button(root, text="The grab button", command=grab_click)
button1.pack()
button2.pack()
button3.pack()

root.mainloop()