import sys , os
# This file contains the functions that are used to save the history of the user's input and output.

def save(str):
    f = open("output.txt", "a")
    f.write(str + "\n")
    f.close()

def history():
    f = open("output.txt", "r")
    str = f.read()
    f.close()
    return str
