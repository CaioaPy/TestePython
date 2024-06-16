from tkinter import *

root = Tk()

def Regular_click():
    label = Label(root, text="You clicked a button.")
    label.pack()

button1 = Button(root, text="The Button", command=Regular_click)
button2 = Button(root, text="The broken Button", state=DISABLED)
button3 = Button(root, text="The BIG Button", padx=100, pady= 100, command=Regular_click)
button1.pack()
button2.pack()
button3.pack()

root.mainloop()