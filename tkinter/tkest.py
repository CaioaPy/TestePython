from tkinter import *

root = Tk()

# create
l1 = Label(root, text="home\n \n\n\nhello")
l2 = Label(root, text="hello again!")
l3 = Label(root, text="owo")
button1 = Button(root, text="test!!")
# then putting it on screen
l1.grid(row=0, column=0)
l2.grid(row=1, column=1)
l3.grid(row=3, column=3)
button1.grid(row=2, column = 2)

root.mainloop()