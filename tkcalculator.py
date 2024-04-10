from tkinter import *

root = Tk()
root.title("Calculator")

Vtext = ""
title = Label(root, text= Vtext)

def click1():
    Vtext = "1"
def click2():
    Vtext = "2"
button1 = Button(root, text="1", padx=35, pady=35, command= click1)
button2 = Button(root, text="2", padx=35, pady=35, command= click2)
button3 = Button(root, text="3", padx=35, pady=35)
button4 = Button(root, text="4", padx=35, pady=35)
button5 = Button(root, text="5", padx=35, pady=35)
button6 = Button(root, text="6", padx=35, pady=35)
button7 = Button(root, text="7", padx=35, pady=35)
button8 = Button(root, text="8", padx=35, pady=35)
button9 = Button(root, text="9", padx=35, pady=35)
button0 = Button(root, text="0", padx=35, pady=35)


title.grid(row=0 , column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=1)

root.mainloop()