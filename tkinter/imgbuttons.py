from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("wow")
icon_img = ImageTk.PhotoImage(Image.open("A.JPEG"))
root.iconbitmap(icon_img)



root.mainloop()