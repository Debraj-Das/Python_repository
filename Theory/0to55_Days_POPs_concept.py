# import sys
# import os
# import math
# if os.environ.get('ONLINE_JUDGE') == None:
#     sys.stdin = open('input.txt', 'r')  # input.txt: name of input file

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



#* Day 16 of 100 days of code
# Match case statement in python
# it is include from python 3.10 version
print("\nMatch case statement in python")
x = 0
match x:
    case 0 :        # value match case
        print("x is Zero")
    case 4 if x**3 == 64 : # value match with if condition
        print("number is 4")
    case _ if x< 0 : # default with if condition
        print("number is native")
    case _ :    # default statement
        print("it is any number ")


# * Day 17 of 100 days of Code
# For loop in python
color = ["red", "green", "blue", "yellow"]
for c in color:
    print(c)
    for i in c: # nested for loop
        print(i, end=' ')
    print('\n')

i = 23 
for j in range(i): # it will print the number from 0 to i-1 or for(i=0;i<23;i++) as C language
    print(j, end=' ')
print('\n')
for i in range(4, 23): # it will print the number from 4 to 22 
    print(i, end=' ')
print('\n')
for i in range(0, 23, 2): # it will print the number from 0 to 22 with step of 2
    print(i, end=' ')

#* Day 18 of 100 days of Code
# while loop in python and while else statement
count = 5 
while (count>0):    # while loop
    print(count)
    count -= 1
else:            # else statement with while loop
    print('count is zero')


# * Day 19 of 100 days of Code
# break and continue statement in python
print("\nbreak and continue statement in python")
n = 23
for i in range(n):
    if (i == 10):
        print("skip the number 10")
        continue  # continue statement
    if (i == 19):
        print("break the loop after 19")
        break  # break statement
    print(i, end=' ')
print('\n')


# * Day 20 of 100 days of Code
# Function in python
# Function is a block of code which is used to perform a specific task and it is reusable
# it is used to make the code more readable and manageable and reduce the code redundancy
# There are two types of function in python i.e. built-in function and user defined function
print("\nFunction in python")


def function_name(parameter): # function definition and you can pass the any parameter in function and it is optional
    # function body
    value = parameter*parameter
    return value # return statement

# function call
parameter = 10
print(function_name(parameter))

# * Day 21 of 100 days of Code
# Function argument in python
# there are four type of argument in python i.e. positional/required argument, keyword argument, default argument and variable length argument


def function_name(name, age):  # positional/required argument
    print("name : ", name)
    print("age : ", age)


function_name("Rahul", 23)  # positional/required argument


def function_name1(name, age=23):  # default argument is age
    print("name : ", name)
    print("age : ", age)


function_name1("Rahul")  # default argument is age


def function_name2(name, age):  # keyword argument
    print("name : ", name)
    print("age : ", age)


function_name2(age=23, name="Rahul")  # keyword argument


def function_name3(*name):  # variable length argument, it take argument as tuple
    print("name : ", name)


function_name3("Rahul", "Raj", "Rohan")


def function_name4(**name):  # variable length argument, it take argument as dictionary
    print("name : ", name)


function_name4(name1="Rahul", name2="Raj", name3="Rohan")

# * Day 22 of 100 days of Code
# List in python and list method and list comprehension and List indexing and slicing
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Rahul", "Raj", "Rohan",["sk", "rk", "pk"]]
print(type(lst),lst)

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:  # in operator
    print("Yellow is present.")
else:
    print("Yellow is absent.")

# these are the list method like string method
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::3])		#using positive indexes and jump by 3
print(animals[-8:-1:2])	#using negative indexes and jump by 2

# List comprehension and syntax is [expression for item in list if condition]
# it used to create the list in one line from existing list or any iterable
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


#* Day 23 of 100 days of Code
# list method like append(), insert(), extend(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()
l = [8 , 23 , 24 ,11 , 42 , 14 , 1441 , 145, 1455, 625, 24]
print(l)
l.append(324) # append() method is used to add the element at the end of the list
print(l)
l.insert(2, 23) # insert() method is used to add the element at the given index
print(l)
l.sort() # sort() method is used to sort the list in ascending order
print(l)
l.sort(reverse=True)
print(l)
l.reverse() # reverse() method is used to reverse the list
print(l)
print(l.index(23)) # index() method is used to find the index of the element
print(l.count(23)) # count() method is used to count the number of occurrence of the element
m = l # reference of the list . so if I change hte value of m then it will also change the value of l
m = l.copy() # copy() method is used to copy the list
m = [900 , 204 , 1344]
l.extend(m)
print(l)
k = m+l # it will concatenate the two list and store in k
print(k)
# like those method there are some more method like remove(), pop(), clear() etc.

#* Day 24 of 100 days of Code
# Tuple in python and tuple method and tuple indexing and slicing
# tuple is immutable and it is ordered and it is represented by ()
# it is same as list but it is immutable
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, "Rahul", "Raj", "Rohan")
print(tup)
print(tup[1:5]) # tuple slicing and indexing is same as list and return the new tuple


#* Day 25 of 100 days of Code
# Tuples are immutable, hence if you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

# but you can concatenate the two tuple directly
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# But those method no change the original tuple , that can be use on the tuple like count(), index() etc.
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
# tuple.index(element, start, end)
res = Tuple1.index(3)
print('First occurrence of 3 is', res)


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

#* Day 27 of 100 days of Code
# Exercise 3 : Kanun Banega Crorepati (KBC)
print("Welcome to KBC")
print("You have 15 question to win 1 crore rupees")
print("You have 4 option for each question")
print("Your name is : ", end=" ")
name = input()
w.write("Name : " + name + "\n")
your_money = 0
question_price = 1000
while(question_price < 10000000):
    if(Question()):
        your_money += question_price
        print("Right Answer")
        print("Your money : ", your_money)
    else:
        print("Wrong Answer")
        print("You lose")
        if(your_money > 1000000):
            your_money = 1000000
        else :
            your_money = 1000
        break
    print("you want to continue (y/n) : ", end=" ")
    choice = input().upper()
    if(choice == "N"):
        print("Now you want to leave the game")
        break
    question_price *= 2


if(question_price < 10000000):
    print("Your money : ", your_money)
    w.write("Money : " + str(your_money) + "\n\n")
else:
    print("Congratulation you won 1 crore rupees")
    w.write("Money : 10000000\n")
f.close()
f.close()


#* Day 28 of 100 days of Code
# f-string in python
name = "Debraj Das"
age = 34
print(f"Hello {name} your age is {age}") # f-string is used to print the variable in the string
print(f"Hello {{name}} your age is {age+2}") # we can also perform the operation in the f-string
number = 230.2345678
print(f"your number is {number:.6f}") # we can also format the number in the f-string like c language

#* Day 29 of 100 days of Code
# Docstring in python and Zen of python
def add(a, b):
    #This function takes two number and return their sum#  #* There # place triple double quote and writting the docstring
    return a+b
# here ''' ''' is called docstring and it is used to describe the function and it is optional
# docsting is used to describe the function , module , class etc.

print(add(2, 3))
print(f"print the docstring of the function add : {add.__doc__}") # we can print the docstring of the function like this

import this # Zen of python is a poem of python and it is written by Tim Peters


# * Day 30 of 100 days of Code
# Recursion in python and factorial of a number using recursion and Exercise 4 : Fibonacci Series


def factoraial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return (num*factoraial(num-1))


print(factoraial(5))  # factorial of a number using recursion

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


# * Day 31 of 100 days of Code
# set in python
# set is a collection of non-repetitive element and it is unordered
s = {23, 23, 133, 31, 13, 42, 23, 315, 55, 13}
print(s)
a = {}
print(type(a))  # this is not a set , this is a dictionary
a = set()  # this is a empty set
print(type(a))

# * Day 32 of 100 days of Code
# Methods of set
# add() , update() , copy() , remove() , del()
# discard() , pop() , clear()
# union() , intersection() , difference() , symmetric_difference(), symmetric_difference_update() 
# intersection_update() , difference_update() , union_update(), 
# issubset() , issuperset() , isdisjoint()
# len() , min() , max() , sum()

a = {23, 23, 133, 31, 13, 42, 23, 315, 55, 13, 5634, 3567, 2567, 7873, 736}
b = {23, 13, 42, 55, 13, 23, 133, 31, 13, 42, 23, 315, 55, 13, 242, 2452, 1414, 42565}

a.add(100)  # add() method is used to add a element in the set
print(a)
a.update([1, 2, 3, 4, 5, 6, 7, 8, 9])  # update() method is used to add multiple element in the set
print(a)
d = a # this is not a copy , this is a reference
c = a.copy()  # copy() method is used to copy a set
print(c)
c.remove(100)  # remove() method is used to remove a element from the set
print(c)
c.discard(200)  # discard() method is used to remove a element from the set and diff is remove() method give a error if the element is not present in the set but discard() method not give any error
print(c)
c.pop()  # pop() method is used to remove a element from the set but it remove the last element from the set
print(c)
c.clear()  # clear() method is used to clear the set
print("it clear the set : ", c)
# c.del()  # del() method is used to delete the set
c = a.union(b)  # union() method is used to find the union of two set and return a new set
print(c)
c = a.intersection(b)  # intersection() method is used to find the intersection of two set and return a new set
print(c)
c = a.difference(b)  # difference() method is used to find the difference of two set and return a new set
print(c)
a.difference_update(b)  # difference_update() method is used to find the difference of two set and update the set
print(a)
c = a.symmetric_difference(b)  # symmetric_difference() method is used to find the symmetric_difference of two set and return a new set
print(c)
print(a.issubset(b))  # issubset() method is used to check a set is subset of another set or not
print(a.issuperset(b))  # issuperset() method is used to check a set is superset of another set or not
print(a.isdisjoint(b))  # isdisjoint() method is used to check a set is disjoint of another set or not
print(len(a))  # len() method is used to find the length of the set
print(min(a))  # min() method is used to find the minimum element of the set
print(max(a))  # max() method is used to find the maximum element of the set
print(sum(a))  # sum() method is used to find the sum of the element of the set


#* Day 33 of 100 days of Code
# Dictionary in python and access the element of the dictionary
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
# I. Accessing single values:
print(info['name']) # if name is not present in the dictionary then it give a error
print(info.get('eligible')) # if eligible is not present in the dictionary then it give a None

# II. Accessing multiple values:
print(info.values()) # values() method is used to print the values of the dictionary

# III. Accessing all the keys:
print(info.keys()) # keys() method is used to print the keys of the dictionary

# IV. Accessing all the items:
print(info.items()) # items() method is used to print the items of the dictionary

#* Day 34 of 100 days of Code
# Methods of dictionary
# some methods are same as the set like -> copy() , clear() , del() , pop() , popitem() , update() , get() , values() , keys() , items() , len() , min() , max() , sum()
# fromkeys() , setdefault() , fromkeys() , has_key() , viewitems() , viewkeys() , viewvalues()
a = {'name':'Karan', 'age':19, 'eligible':True}
a.update({'name':'Karan Singh'}) # update() method is used to update the dictionary
a.pop('age') # pop() method is used to remove a element from the dictionary
a. popitem() # popitem() method is used to remove a last element from the dictionary
del a['eligible'] # del() method is used to delete a element from the dictionary
# del a # del() method is used to delete the dictionary
# there are many methods in dictionary so for that used official documentation of python
# dictioanry is a collection of key-value pair and it is unordered and unindexed and it is mutable
# it is very used full in the real world application because real life database like mysql , mongodb , etc. is store the data in the form of key-value pair


#* Day 35 of 100 days of Code  
# for loop with else statement
# else execute when the for loop is completed and not execute when the for loop is break
for i in range(9):
    print(i)
else:
    print("this is else statement of for loop")

for i in range(12):
    print(i+1)
    if(i==5):
        break
else:
    print("this is else statement of for loop")
print("this is outside of for loop")

# similarly while loop with else statement also work (executed when the while loop is completed and not executed when the while loop is break)


# * Day 36 of 100 days of Code
# Try and Except in python
try:
    a = int(input("Enter a number : "))
except Exception as e:  # except statement is executed when the try statement is not executed successfully and it is used to handle the error and there are many types of error in python like ValueError , TypeError , IndexError , etc.
    # e is a object of Exception class and it is used to print the error
    print("Error : ", e)
except:    # You can also use except statement without Exception class and add multiple except statement
    print("Error : Enter a valid number")
else:  # else statement is executed when the try statement is executed successfully
    print("\nEnter number is : ", a)
    print("This is else statement of try and except")
finally:  # finally statement is executed when the try statement is executed successfully or not and it is used to execute the code that is always executed
    print("This is finally statement of try and except")

print("This is outside of try and except")


#* Day 37 of 100 days of Code
# Finally statement in python
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0
  finally:  # finally statement is executed when the try statement is executed successfully or not 
    #and it is used to execute the code that is always executed and it is used to close the file and database connection
    # and it is used to release the resources and execute the code that is always executed 
    # it execute the code before the return statement of this function
    # that is difference between finally and general code after try and except statement
    print("I am always executed")
  # print("I am always executed")

x = func1()
print(x)


#* Day 38 of 100 days of Code
# Raise Exception in python
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary") # raise statement is used to raise the exception and it is used to raise the exception manually
# ValueError is a class of exception and it is used to raise the exception manually
# there are many types of exception in python like ValueError , TypeError , IndexError , etc.
# And also you can create your own exception class like
class CustomError(Exception):
  # code ...
  pass

# How to use custom exception class
try:
  # code ...
  pass
except CustomError:
  # code...
  pass


#* Day 39 of 100 days of Code
# In this day we try to check the KBC game solution in python

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
    
    
#* Day 41 of 100 days of Code
# Short Hand if else

a = 330 
b = 330

if a>b: 
    print("a")
elif a==b:
    print("equal")
else:
    print("b")
    
# Short Hand if else
print("a") if a>b else print("equal") if a==b else print("b")

vaule = a if a>b else b # this is also a short hand if else statement
print(vaule)

#* Day 42 of 100 days of Code
# Enumerate function in python

marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")
print('\n')

l = [321,424,13452,524,3,624,36,24,256,2,156,35,1245,36,52,5365256,5,25,6,255,2,5,2525,24]
for i , mark in enumerate(l , start=1):
    print(i , mark)
# enumerate function is used to iterate the list and tuple and it is used to return the index and value of the list and tuple
# start is used to start the index from the given number and default value of start is 0 but you can change it


#* Day 43 of 100 days of Code
# Virtual Environment
# https://replit.com/@codewithharry/43-Day43-Virtual-Environment#.tutorial/Tutorial.md
# virtual environment is used to create the virtual environment for the project and it is used to install the package in the virtual environment
# The "requirements.txt" file
# The requirements.txt file is used to store the package name and version of the package and it is used to install the package in the virtual environment

#* Day 44 of 100 days of Code
# How import works in python
import math

print(dir(math)) # dir function is used to print the all the function and variable of the module
print(math.__doc__) # __doc__ is used to print the documentation of the module
print(math.__name__) # __name__ is used to print the name of the module

result = math.sqrt(9) # sqrt is a function of math module and it is used to find the square root of the number
print("The square root of 9 is ",result)

# import math as m # you can also use alias name of the module
# from math import sqrt, pow # you can also import the specific function of the module
# from math import * # you can also import all the function of the module


#* Day 45 of 100 days of Code
# main function in python

if __name__ == "__main__": # this is used to check the main function in python
    print("Hello World")
    print("This is main function")
    print("My name is Debraj Das")


import Rough as r   # import the module and if any gobal variable, statement is present in the module then it is executed
# so always use the main function in the module

i = r.inp()
print("The value of i is",i)
print(dir(r))   # dir function is used to print the all the function and variable of the module
print(r.__doc__) # __doc__ is used to print the documentation of the module


#* Day 46 of 100 days of Code
# OS module in python (it is very very important module in python)
## https://docs.python.org/3/library/os.html (this is the official documentation of the os module in python)
# This module provides a portable way of using operating system dependent functionality.
# this create a folder in the current directory and create 100 folder in the folder with name Day(i+1) where i is the index of the loop
import os

if(not os.path.exists("data")):
    os.mkdir("data")

# it create 100 folder in the data folder
for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")
# it delete the 100 folder in the data folder
for i in range(0, 100):
    os.rmdir(f"data/Day{i+1}")
    
if (os.path.exists("data")):
    os.rmdir("data")


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


#* Day 48 of 100 days of Code
# Gobal and local variable in python
x = 10 # this is a gobal variable
z = 2345 # this is a gobal variable
def hell():
    global x # this is a gobal variable
    x = 20
    y = 234 # this is a local variable
    print("The value of x inside function is",x)
    print("The value of y inside function is",y)
    print("The value of z inside function is",z)

print("The value of x outside function before the call the hell function is",x)
hell()
print("The value of x outside function is",x)

# But it is not a good practice to use the gobal variable inside the function
# but if you want to use the gobal variable inside the function then you can use the global keyword


# * Day 49 of 100 days of Code
# File OI in python
# f = open("input.txt", 'r')  # open the file in read mode
# content = f.read()  # read the whole content of the file and there are many function to read the file e.g. read(), readline(), readlines()
# print(content)
# f.close()  # close the file
import os
if (not os.path.exists('name.txt')):
    f = open("name.txt",'x') # create a file
    f.close()

# if (os.path.exists('name.pdf')):
#     os.remove("name.pdf") # remove the file


#* Day 50 of 100 days of Code   
#read() , readline() , writeline() , write() , tell() , seek() , close() , readlines() method in python
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()


# * Day 51 of 100 days of Code
# seeks() , tell() , other method in python

# seek() method is used to move the cursor in the file
with open('input.txt', 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)
    print(data)

# tell() method is used to tell the current position of the cursor in the file
with open('input.txt', 'r') as f:
    # Read the first 10 bytes
    data = f.read(10)
    print(data)

    # Save the current position
    current_position = f.tell()
    print(current_position)

    # Seek to the saved position
    f.seek(current_position+2)
    print(f.read(5))

# truncate() method is used to truncate the file
with open('input.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(7)

with open('input.txt', 'r') as f:
  print(f.read())



# * Day 52 of 100 days of Code
# lambda function in python
# def double(x):
#   return x*2
double = lambda x: x * 2 # this is a lambda function and it is also called anonymous function
# lambda function is used to create a function in one line
# double function can be def both way

def appl(fx, value):
  return 6 + fx(value)

cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))

p = lambda x , y : print(f'{x} and {y} = {x+y}')

p(2, 3) # you pass this function to other function as a argument



# * Day 53 of 100 days of Code
# Map , Filter , Reduce function in python (**it is very very important)
# Map function is used to apply a function to all the elements of a list
l = [1, 2, 3, 4, 5, 24, 2, 14, 5, 4, 36,
     4, 14, 545, 6, 251, 4, 26, 5, 14, 51, 242]
newl = list(map(lambda x: x**2, l))
# this is a map function and it is used to apply a function to all the elements of a list

for i in newl:
    print(i, end=' ')
print('\n')

# Filter function is used to filter the elements of a list
newl = list(filter(lambda x: x > 5, l))

for i in newl:
    print(i, end=' ')
print('\n')

# Reduce function is used to reduce the elements of a list
from functools import reduce
new = reduce(lambda x, y: x+y, l) # this is a reduce function and it is used to reduce the elements of a list
print(new)


# * Day 54 of 100 days of Code
# is vs == operator in python
a = None    # None is a special type in python , so it has only one instance or memory location
b = None
print(a is b)  # exact location of object in memory
print(a is None)  # exact location of object in memory
print(a == b)  # value

a = [1, 2, 3]  # list is a mutable object in python
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

a = "hello"  # string is a constant value in python
b = "hello"
print(a == b)  # True
print(a is b)  # True

a = 5  # integer is a constant value in python
b = 5
print(a == b)  # True
print(a is b)  # True
# for constant value python use the same memory location
# is and == operator give same result for constant value
# is operator is used to check the exact location of object in memory
# == operator is used to check the value of object


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

'''
