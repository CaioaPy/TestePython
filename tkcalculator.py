from tkinter import *

root = Tk()
root.title("Calculator")

title = Label(root, text="calculator")
button1 = Button(root, text="1", padx=35, pady=35)
button2 = Button(root, text="2", padx=35, pady=35)
button3 = Button(root, text="3", padx=35, pady=35)


title.grid(row=0 , column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

root.mainloop()