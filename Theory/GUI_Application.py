""" 
# some part present for the practise and Revision of tkinter module
# Try to completed by fast as possible
Video links : https://www.youtube.com/watch?v=YXPyB4XeYLA

This is the first GUI application using tkinter module in python.
In the Tkinter module's documentation, you can find a list of all the different widgets available.
1. Label: A Label widget shows text to the user. It can also be used to display an image.
2. Button: A Button widget is used to display a button on the screen. It can contain text and images.
3. Entry: An Entry widget is used to accept single-line text strings from a user.
4. Text: A Text widget is used to display multi-line text to the user.
5. Frame: A Frame widget is used as a container widget to organize other widgets.
6. Checkbutton: A Checkbutton widget is used to display a number of options to a user as toggle buttons. The user can select multiple options at a time.
7. Radiobutton: A Radiobutton widget is used to display a number of options to a user as radio buttons. The user can select only one option at a time.
8. Scale: A Scale widget is used to select from a range of values. It provides a slider that can be dragged by the user to select a value from the given range.
9. Listbox: A Listbox widget is used to display a list of options to a user. The user can select one or multiple options at a time.

Some propreties of root window: title, iconbitmap, geometry, resizable, minsize, maxsize

text (str) - The text to be displayed on the label.
button -> button widget on the screen
input -> entry widget on the screen, which take input from user
frame(like container) -> frame widget on the screen(like container in screen and partition of total screen)
checkbutton , radiobutton -> yes or no type button
scale(like slider) -> scale widget on the screen(like slider)
listbox(like dropdown) -> listbox widget on the screen
filedialog -> filedialog widget on the screen
folderdialog -> folderdialog widget on the screen

*image -> PIL
*PDF -> PyPDF2
*Video -> moviepy
*Database -> sqlite3
*API -> requests
*Graph -> matplotlib
*Excel -> openpyxl


#In tkinter module , first define the widget and then pack(or grid) it on the screen.

"""

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
