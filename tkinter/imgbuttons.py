from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("wow")
root.iconbitmap('C:/Users/User/Documents/programa acao/TestePython/tkinter/img/0v0.ico')

buttonA = Button(text="a")
imgA = ImageTk.PhotoImage(Image.open("A.JPEG"))

buttonA.pack()

root.mainloop()