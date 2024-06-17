from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=30)

Result = 0
sumV = 0
minusV = 0
divideV = 0
multiplyV = 0

def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def clear():
    e.delete(0, END)
    e.insert(0, " ")

def sum():
    sumV += 1
    e.delete(0, END)
    e.insert(0, " ")

def minus():
    minusV += 1
    e.delete(0, END)
    e.insert(0, " ")

def divide():
    divideV += 1
    e.delete(0, END)
    e.insert(0, " ")

def multiply():
    multiplyV += 1
    e.delete(0, END)
    e.insert(0, " ")

def result():
    if (sumV == 1)

button1 = Button(root, text="1", padx=35, pady=35, command=lambda: click(1))
button2 = Button(root, text="2", padx=35, pady=35, command=lambda: click(2))
button3 = Button(root, text="3", padx=35, pady=35, command=lambda: click(3))
button4 = Button(root, text="4", padx=35, pady=35, command=lambda: click(4))
button5 = Button(root, text="5", padx=35, pady=35, command=lambda: click(5))
button6 = Button(root, text="6", padx=35, pady=35, command=lambda: click(6))
button7 = Button(root, text="7", padx=35, pady=35, command=lambda: click(7))
button8 = Button(root, text="8", padx=35, pady=35, command=lambda: click(8))
button9 = Button(root, text="9", padx=35, pady=35, command=lambda: click(9))
button0 = Button(root, text="0", padx=35, pady=35, command=lambda: click(0))
buttonAdd = Button(root, text="+", padx=35, pady=35, command=lambda: click("+"))
buttonSub = Button(root, text="-", padx=35, pady=35, command=lambda: click("-"))
buttonDiv = Button(root, text="/", padx=35, pady=35, command=lambda: click("/"))
buttonMul = Button(root, text="*", padx=35, pady=35, command=lambda: click("*"))
buttonClear = Button(root, text="C", padx=35, pady=35, command=lambda: clear())
buttonResult = Button(root, text="=", padx=70, pady=35, command=lambda: result())

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=1)
buttonAdd.grid(row=0, column=3)
buttonSub.grid(row=1, column=3)
buttonDiv.grid(row=2, column=3)
buttonMul.grid(row=3, column=3)
buttonClear.grid(row=0, column=2)
buttonResult.grid(row=4, column=2, columnspan=2)

root.mainloop()