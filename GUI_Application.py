from tkinter import *
import os
from tkinter import filedialog

root = Tk()
root.title("My First GUI Application")
root.iconbitmap("icon.ico")


def openfolder():
    folders_path = filedialog.askdirectory()
    os.chdir(folders_path)
    print(os.getcwd())

folder = Button(root, text="Open Folder", command=openfolder)
folder.grid(row=1, column=1)
# str = "My first GUI Application\n It is very very simple things to do\n I am doing for destop appilation\n"

# e = Entry(root, width=50, bg="white", fg="blue",
#           borderwidth=5, font=("Helvetica", 30))
# e.pack()


# def func():
#     mylebel = Label(root, text="Hello " + e.get() , font=("Helvetica", 30))
#     mylebel.pack()

# Creating a Label Widget
# myLabel1 = Label(root, text=str)
# myLabel2 = Label(root, text="My first GUI Application")

# Shoving it onto the screen

# packing things
# myLabel.pack()

# Grid system for placing things
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=2, column=0)


# mybotton = Button(root, text="Click Me", command=func, fg="blue", bg="red" , font=("Helvetica", 30))

# mybotton.pack()



# button_quit = Button(root, text="Exit", command=root.quit)
# button_quit.pack()

# For image use PhotoImage for GUI application

# from PIL import ImageTk, Image

# my_img = ImageTk.PhotoImage(Image.open("dragon.jpg"))
# my_label = Label(image=my_img)
# my_label.pack()






root.mainloop()
