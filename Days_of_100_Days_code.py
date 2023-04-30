import sys
import os
import math
if os.environ.get('ONLINE_JUDGE') == None:
    sys.stdin = open('input.txt', 'r')  # input.txt: name of input file

'''
#* Day 4 of 100 days of code
# First code written in python
print("\n Days 4 : First code written in python")
print("--- Your peom is here ---")

#* Day 5 of 100 days of code
# Escape sequence characters in python '/n' and '/t' etc.
# comments and multi line comments  single # and  multi ''' ''' or """ """
# print function arugments sep and end and comma saparated values like e.g.
print("\n Days 5 : Escape sequence characters in python")
print("Hello \nWorld", 4 , 34.32 , sep='~', end='323\n\n')
print("Hello world")

#* Day 6 of 100 days of code
# Variable and Data types
# in python we don't need to declare variable type and all the data type is object 
# There are 5 standard data types -> Numbers, String, List, Tuple, Dictionary
# Numbers -> int, float, complex
# String -> str , List -> list , Tuple -> tuple , Dictionary -> dict
# type() function is used to find the type of variable and id() function is used to find the address of variable
# list is mutable and tuple is immutable
print("\n Days 6 : Variable and Data types")
a = 3
print(a, type(a))
a = 3.4 
print(a, type(a))
a = 3 + 4j
print(a, type(a))
a = "Hello"
print(a, type(a))
a = [1, 2, 3, "Hello", [1, 2]] 
print(a, type(a))
a = (1, 2, 3, "Hello", (1, 2))
print(a, type(a))
a = {1: "Hello", 2: "World", 3: [1, 2, 3]}
print(a, type(a))

#* Day 7 of 100 days of code
# Arithmatic Operators e.g +, -, *, /, %, //, **
print("\n Days 7 : Arithmatic Operators")
a = 5
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # modulus
print(a // b) # floor division
print(a ** b) # power


#* Day 8 of 100 days of code
# soultion of Exercise 1 : calculator 
print("\n Days 8 : Exercise 1 : calculator")
a = 12 
b = 34
print("Sum of 12 and 34 is : ", a + b)
print("Subtraction of 12 and 34 is : ", a - b)
print("Multiplication of 12 and 34 is : ", a * b)
print("Division of 12 and 34 is : ", a / b)

#* Day 9 of 100 days of code
# Type casting in python (Implicitly and Exclicitly)
a = "23"
b = "34"
print("Sum of 23 and 34 is : ", int(a) + int(b)) # type casting string to int Exclicitly
a = 3.5
b = 3 
print("Sum of 3.5 and 3 is : ", a+b) # type casting int to float Implicitly

#* Day 10 of 100 days of code
# Take input from user in python 
# input() function take input as string so we need to type cast it convert according to our need
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
print("Sum of ", a, " and ", b, " is : ", a+b)

# * Day 11 of 100 days of code
print("\n String in python")
print("\nMulti line string : ")
s = # this is the 
sldjfi 
 sdfksjeoif
  lsjfoiwj  2425v 224 , you can write multi line string using triple quote # (# is actually tirple quote)
print(s)

print("\nsingle quote : ")
s = 'wefw wefq qer ' # single quote string
print(s)
print("\ndouble quote : ")
s = "wefw wefq qer " # double quote string
print(s)

#* Day 12 of 100 days of code
# String Slicing and Operations on string in python
print("\n String Slicing and Operations on string in python")
name = "Debraj Das"
print(name[1:3]) # string slicing
print(len(name)) # len() function is used to find the length of string
print(name[-6:-1]) # negative index start from -1 and goes to -n where n is length of string where -1 is last character of string or you can map -a to n-a where a is any positive number


#* Day 13 of 100 days of code
# String Methods in python
str1 = "Welcome to the console"
print(str1.upper()) # upper() method is used to convert string to upper case
print(str1.lower()) # lower() method is used to convert string to lower case
print(str1.title()) # title() method is used to convert string to title case
print(str1.count("o")) # count() method is used to count the number of occurance of a character in string
print(str1.find("o")) # find() method is used to find the index of first occurance of a character in string
print(str1.replace("o", "0")) # replace() method is used to replace a character with another character in string
print(str1.split(" ")) # split() method is used to split the string into list of string according to the character passed as argument
print(str1.strip()) # strip() method is used to remove the white space from the string
print(str1.isalnum()) # isalnum() method is used to check if the string is alphanumeric or not
print(str1.isalpha()) # isalpha() method is used to check if the string is alphabetic or not
print(str1.isdigit()) # isdigit() method is used to check if the string is digit or not
print(str1.islower()) # islower() method is used to check if the string is in lower case or not
print(str1.isupper()) # isupper() method is used to check if the string is in upper case or not
print(str1.isspace()) # isspace() method is used to check if the string is space or not
print(str1.startswith("W")) # startswith() method is used to check if the string start with the character passed as argument or not
print(str1.endswith("e")) # endswith() method is used to check if the string end with the character passed as argument or not
print(str1.endswith("co", 0, 10)) # endswith() method is used to check if the string end with the character passed as argument or not in the range of index passed as argument
print(str1.join("123")) # join() method is used to join the string with the character passed as argument
print(str1.capitalize()) # capitalize() method is used to capitalize the first character of string
print(str1.swapcase()) # swapcase() method is used to swap the case of string
print(str1.center(50)) # center() method is used to center the string according to the number passed as argument
print(str1.encode()) # encode() method is used to encode the string
print(str1.expandtabs()) # expandtabs() method is used to expand the tab in string
print(str1.format()) # format() method is used to format the string
print(str1.index("o")) # index() method is used to find the index of first occurance of a character in string
print(str1.isdecimal()) # isdecimal() method is used to check if the string is decimal or not
print(str1.isidentifier()) # isidentifier() method is used to check if the string is identifier or not
print(str1.isprintable()) # isprintable() method is used to check if the string is printable or not
print(str1.ljust(50)) # ljust() method is used to left justify the string according to the number passed as argument
print(str1.lstrip()) # lstrip() method is used to remove the white space from the left side of string
print(str1.maketrans("o", "0")) # maketrans() method is used to make a translation table
print(str1.partition("o")) # partition() method is used to partition the string according to the character passed as argument
print(str1.rfind("o")) # rfind() method is used to find the index of last occurance of a character in string
print(str1.rindex("o")) # rindex() method is used to find the index of last occurance of a character in string
print(str1.rjust(50)) # rjust() method is used to right justify the string according to the number passed as argument
print(str1.rpartition("o")) # rpartition() method is used to partition the string according to the character passed as argument
print(str1.rsplit("o")) # rsplit() method is used to split the string into list of string according to the character passed as argument
print(str1.rstrip()) # rstrip() method is used to remove the white space from the right side of string
print(str1.translate("o")) # translate() method is used to translate the string according to the character passed as argument
print(str1.zfill(50)) # zfill() method is used to fill the string with 0 according to the number passed as argument
print(str1.isascii()) # isascii() method is used to check if the string is ascii or not
print(str1.casefold()) # casefold() method is used to convert the string to casefold
print(str1.format_map("o")) # format_map() method is used to format the string according to the character passed as argument


#* Day 14 of 100 days of code
# if else statement in python 
print("\nif else statement in python")
a = int(input("Enter a number : "))
if(a<0):
    print("Negative number")
elif(a==0):
    print("Zero")
else:
    print("Positive number")
    if(a%2==0): # nested if else statement
        print("Even number")
    else:
        print("Odd number")
        

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

'''

#* Day 16 of 100 days of code
# Match case statement in python
print("\nMatch case statement in python")

