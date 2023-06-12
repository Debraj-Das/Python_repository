import sys
import os
import math
if os.environ.get('ONLINE_JUDGE') == None:
    sys.stdin = open('input.txt', 'r')

'''
#* Day 8 of 100 days of code
# soultion of Exercise 1 : calculator 
print("\n Days 8 : Exercise 1 : calculator")
a = 12 
b = 34
print("Sum of 12 and 34 is : ", a + b)
print("Subtraction of 12 and 34 is : ", a - b)
print("Multiplication of 12 and 34 is : ", a * b)
print("Division of 12 and 34 is : ", a / b)


# * Day 15 of 100 days of code
# Exercise 2 : Good Morning Sir/Madam
print("\nExercise 2 : Good Morning Sir/Madam")
import time
timestamp = int(time.strftime("%H"))
print(time.strftime("%H:%M:%S"))
if (timestamp < 12):
    print("Good Morning Sir/Madam")
elif (timestamp < 16):
    print("Good Afternoon Sir/Madam")
elif (timestamp < 20):
    print("Good Evening Sir/Madam")
else:
    print("Good Night Sir/Madam")



# * Day 26 of 100 days of Code
# Exercise 3 : Kanun Banega Crorepati (KBC)
# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

f = open("input.txt", "r")
w = open("output.txt", "w")

def Question():
    # Read the question and option from the file
    if(f.readline() == ""):
        return False
    else :
        print("Question :")
    question = f.readline()
    o1 = f.readline()
    o2 = f.readline()
    o3 = f.readline()
    o4 = f.readline()
    # Print the question and option
    print(question, o1, o2, o3, o4)
    # Read the answer from the file
    ans = f.readline()
    ans = ans[0] # Read the first character of the answer
    # Take the answer from the user
    print("Your answer : ", end=" ")
    your_ans = input()
    your_ans = your_ans.upper()
    # print(ans, your_ans)
    if(ans == your_ans):
        return True
    else:
        print("Answer is ", ans)
        return False


# Home work : Fibonacci Series
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 .....


def fibonacci_ser(num):
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return (fibonacci_ser(num-1)+fibonacci_ser(num-2))


print(fibonacci_ser(8))


#* Day 40 of 100 days of Code
# Exercise 4 : Secret code language
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

# Encode part
import string
import random

def ran_3_char():   
    randomLetter = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
    return randomLetter

s = input()
if(len(s)>=3):
    s = s[1:] + s[0]
    s = ran_3_char() + s + ran_3_char()
    s = s[::-1]
else:
    s = s[::-1]

print("Encoded string is : ", s)

# Decode part
if(len(s)<3):
    s = s[::-1]
else:
    s = s[::-1]
    s = s[3:-3]
    s = s[-1] + s[:-1]

print("Decoded string is : ", s)


# * Day 47 of 100 days of Code
# Exercise 4 : solution
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

import string
import random

def ran_3_char():
    randomLetter = random.choice(string.ascii_letters) + random.choice(
        string.ascii_letters) + random.choice(string.ascii_letters)
    return randomLetter

# coding = input("1 for Coding or 0 for Decoding \n")
# coding = True if (coding == "1") else False
coding = False

st = input("Enter message")
words = st.split(" ")
if (coding):
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = ran_3_char() + word[1:] + word[0] + ran_3_char()
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("message after encode : "," ".join(nwords))

else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("message after Decode : "," ".join(nwords))


# * Day 55 of 100 days of Code
# Exercise 5 : Snake Water Gun
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun.
# The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

import random as r
user_score = 0
# 0 for snake , 1 for water , 2 for gun and 3 for see score and other for exit
table = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
print("0 for snake , 1 for water , 2 for gun and 3 for see score and other for exit")
while True :
    user_choice = int(input("Enter your choice (0/1/2) : "))
    if(user_choice == 3):
        print(f"Your score is {user_score}")
    elif(user_choice > 3):
        print(f"Your final score is {user_score}")
        break
    else :
        computer_choice = r.randint(0, 2)
        user_score += table[user_choice][computer_choice]
        if(table[user_choice][computer_choice] == 1):
            print("You win")
        elif(table[user_choice][computer_choice] == 0):
            print("Match draw")
        else :
            print("You lose")

print("Thanks for playing")


# * Day 64 of 100 days of Code
# Exercise 6 : Library Management System
# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods.
# Show that your program doesnt persist the books after the program is stopped!


class Libary:
    # Book = list()   # list of books

    def __init__(self, book_list) -> None:
        self.Book = book_list

    @property
    def books(self):
        print("The books in the library are : ")
        for i, books in enumerate(self.Book):
            print(f'{i+1}. {books}')
        print('\n')

    @books.setter
    def books(self, book_list):
        self.Book.append(book_list)

    def no_of_books(self):
        print("The number of books in the library are : ", len(self.Book))


l = ["Harry Potter", "The Alchemist",
     "The Monk who sold his ferrari", "The 5 AM Club"]

obj = Libary(l)
obj.books
obj.books = "The Secret"
obj.books
obj.no_of_books()


#* Day 67 of 100 days of Code
# Exercise 7 : Clear the Clutter
# Write a program to clear the clutter inside a folder on your computer.
# You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder.
# Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os , glob    # glob is used to find the files with the given extension

# for change the directory
ch = input("Do you want to change the directory (y/n) : ")
if(ch == 'y'or ch == 'Y'):
    path = input("Enter the path of the directory : ")
    os.chdir(path)

extension = input("Enter the extension of the file : ")

for i , file in enumerate(glob.glob(f'*.{extension}'), start=1):
    os.rename(file, f'{i}.{extension}')
    print(f'{file} --> {i}.{extension}')

#* Day 76 of 100 days of Code
# Excersice 8 : PDF Merging
# Merging two or more pdf files into one pdf file
from pypdf import PdfWriter
import os , glob

# for change the directory
l = glob.glob('*.pdf')
merger = PdfWriter()

for pdf in l:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()



#* Day 83 of 100 days of Code
# Exercise 9 : Shoutout in Python
# Write a python program to shoutout to your friends in python using the win32com module.
import win32com.client

# Calling the Dispatch method of the module which interact with Microsoft Speech SDK to speak the given input from list

speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["Debraj", "praveen" , "Aditya" , "Rahul" , "Raj"]

for i in l:
    speaker.Speak(f"Shoutout to {i}")


'''
