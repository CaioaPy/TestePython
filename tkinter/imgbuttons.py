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

buttonA.pack()
buttonB.pack()
buttonC.pack()
buttonD.pack()

root.mainloop()