from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=30)

sumV = 0
minusV = 0
divideV = 0
multiplyV = 0
num1 = 0

def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def clear():
    e.delete(0, END)
    e.insert(0, " ")

def sum():
    global sumV
    sumV += 1
    global num1
    num1 = e.get()
    e.delete(0, END)
    e.insert(0, " ")

def minus():
    global minusV
    minusV += 1
    global num1
    num1 = e.get()
    e.delete(0, END)
    e.insert(0, " ")

def divide():
    global divideV
    divideV += 1
    global num1
    num1 = e.get()
    e.delete(0, END)
    e.insert(0, " ")

def multiply():
    global multiplyV
    multiplyV += 1
    global num1
    num1 = e.get()
    e.delete(0, END)
    e.insert(0, " ")

def result():
    num2 = e.get()
    if (sumV == 1):
        Result = int(num1) + int(num2)
    elif (minusV == 1):
        Result = int(num1) - int(num2)
    elif (divideV == 1):
        Result = int(num1) / int(num2)
    elif (multiplyV == 1):
        Result = int(num1) * int(num2)
    e.delete(0, END)
    e.insert(0, Result)

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
buttonAdd = Button(root, text="+", padx=35, pady=35, command=lambda: sum())
buttonSub = Button(root, text="-", padx=35, pady=35, command=lambda: minus())
buttonDiv = Button(root, text="/", padx=35, pady=35, command=lambda: divide())
buttonMul = Button(root, text="*", padx=35, pady=35, command=lambda: multiply())
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