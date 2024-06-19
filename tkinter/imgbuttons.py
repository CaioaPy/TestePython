from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("wow")
root.iconbitmap('C:/Users/User/Documents/programa acao/TestePython/tkinter/img/0v0.ico')

imgA = ImageTk.PhotoImage(Image.open("A.JPEG"))
imgB = ImageTk.PhotoImage(Image.open("B.JPEG"))
imgC = ImageTk.PhotoImage(Image.open("C.JPEG"))
imgD = ImageTk.PhotoImage(Image.open("D.JPEG"))

buttonA = Button(text="a", image=imgA)
buttonB = Button(text="a", image=imgB)
buttonC = Button(text="a", image=imgC)
buttonD = Button(text="a", image=imgD)

buttonA.grid(row=0, column=0)
buttonB.grid(row=0, column=1)
buttonC.grid(row=1, column=0)
buttonD.grid(row=1, column=1)

root.mainloop()