from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("icons")
root.iconbitmap('C:/Users/User/Documents/programa acao/TestePython/tkinter/img/0v0.ico')


e = Entry(root, borderwidth=3)
e.pack()

img1 = ImageTk.PhotoImage(Image.open("image-w1280.jpg"))
img_label = Label(image=img1)
img_label.pack()

def Regular_click():
    label = Label(root, text="You clicked a button.")
    label.pack()

def grab_click():
    label = Label(root,text=e.get())
    label.pack()

button1 = Button(root, text="The Button", command=Regular_click)
button2 = Button(root, text="The broken Button", state=DISABLED)
button3 = Button(root, text="The grab button", command=grab_click)
quit_button = Button(root, text="Exit", command=root.quit)
button1.pack()
button2.pack()
button3.pack()
quit_button.pack()

root.mainloop()