from tkinter import *

root = Tk()

# create
l1 = Label(root, text="home\n \n\n\nhello")
l2 = Label(root, text="hello again!")
# then putting it on screen
l1.grid(row=0, column=0)
l2.grid(row=14, column=1)

root.mainloop()