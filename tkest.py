from tkinter import *

root = Tk()

# create
l1 = Label(root, text="home\n \n\n\nhello")
l2 = Label(root, text="hello again!")
l3 = Label(root, text="owo")
# then putting it on screen
l1.grid(row=0, column=1)
l3.grid(row=0, column=0)
l2.grid(row=14, column=2)

root.mainloop()