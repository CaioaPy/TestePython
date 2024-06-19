from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("wow")
root.iconbitmap('C:/Users/User/Documents/programa acao/TestePython/tkinter/img/0v0.ico')

iA = Image.open("A.JPEG")
iB = Image.open("B.JPEG")
iC = Image.open("C.JPEG")
iD = Image.open("D.JPEG")

resize_A = iA.resize((400, 400))
resize_B = iB.resize((400, 400))
resize_C = iC.resize((400, 400))
resize_D = iD.resize((400, 400))

imgA = ImageTk.PhotoImage(resize_A)
imgB = ImageTk.PhotoImage(resize_B)
imgC = ImageTk.PhotoImage(resize_C)
imgD = ImageTk.PhotoImage(resize_D)


buttonA = Button(text="a", image=imgA)
buttonB = Button(text="a", image=imgB)
buttonC = Button(text="a", image=imgC)
buttonD = Button(text="a", image=imgD)

buttonA.grid(row=0, column=0)
buttonB.grid(row=0, column=1)
buttonC.grid(row=1, column=0)
buttonD.grid(row=1, column=1)

root.mainloop()