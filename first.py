
#~ This is intial code part of python like- input or output 
# print("Hello world\n")
# print("My name is Debraj Das",end=' ')
# print("Nice to meet you")
# name = input("what is your name :: ")
# print("Nice to meet you", name)
# print("print the first letter :",name[0])
# age = int(input("What is your age :: "))
# age = 89.64
# print(age)
# print(type(age))

#~ This is the Set part implement
# x = {"apple", "banana", "cherry"}   #* set implement like unorder set in STL(Hash table)
# y = {"google", "microsoft", "apple"}

# x.update(y)

# print(x)



#~ string part of impliment
# name = name.upper()
# print("Nice to meet you", name)

#~ list part implement
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# thislist.reverse()
# thislist.append("mango")
# print(thislist)

#~ while loop
# i =0
# while(i<45):
#     print(i)
#     i+=1 

#~ bulit in function
# a =int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))
# c = sum((a,b))  # bulit in function
# print(c)

#~ user defined function

# def function1():            # thus we do not return so ruturn type is none
#     print("Hello everyone")

# function1()


# def average(a , b):
#     """This function use for only two number"""
#     return (a+b)/2

# print(average.__doc__)
# print(average(3,4))

#~ Try except exception Handling

# a = input("Enter a number :: ")
# b = input("Enter a number :: ")
# try:
#     print("Sum of the number is ",int(a)+int(b))
# except Exception as e:
#     print(e)
# print("This line is very importance")

#~ File IO Basics
# f = open("Guess_the_number.py")
# content = f.read()
# print(content)

# for line in f:
#     print(line)
# f.close()

#~ write and read mode 

# f = open("try.txt","r+")
# print(f.read())
# f.write("\nMy name is Debraj\n")
# f.write("thanks bro\n")
# f.close()

#~ for loop 
# n = int(input("Enter the number : "))
# fac = 1
# for i in range(n):
#     fac *= (i+1)
# print(fac)

# #~ function and different type argument
# #* normal and default argument function
# # def fun(a , b , c ,d , e = " nice "):
# #     print(a, b , c , d , e)

# # * call the function
# # fun("name","is","debraj","das")

# '''
#     if you not def any class or function then space are -->
#     behave like global function scope
# '''

# #* args argument and kwargs argument

# def funarg(normal , *args , **kwargs):
#     print(type(args))
#     print(normal)
#     for item in args:
#         print(item)
#     for key, vaule in kwargs.items():
#         print(f"{key} : {vaule} ")      #* f string use inside of print function

# var = ["Deb","raj","Das","Bappy"]

# kw = {"first":1 , "second":2 , "third":3 , "fourth":4}

# funarg("this is normal variable",*var,**kw)

#~ Time module

import time         #* import time module

# i=0
# n = int(input("Enter n : "))
# intial = time.time()
# while(i<n):
#     print('a',end='')
#     i+=1
# print("\nExecution time for while loop : ",time.time()-intial)

# intial = time.time()
# for i in range(5):
#     time.sleep(0.5)   # this is sleep function
#     print('a',end=' ')
# print("\nExecution time for for loop : ",time.time()-intial)

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)


#* Enumerate Function

# ll = ["rice" , "potoal", "vindi","banana"]

# i = 0 
# for item in ll:
#     if(i%2==0):
#         print(f"bhai please : {item} ")
#     i+=1
# alternative method is ::
## enumerate function also return index of that element and it start with zero
# for index , item in enumerate(ll):      
#     if(index%2==0):
#         print(f"bhai please : {item} ")

#* code for print local time of that local area
# import time as t 
# print(t.asctime(t.localtime(t.time())))
# print(t.__doc__)

# import sys
# print(sys.path)

# import debraj
# print(debraj.name)
# from debraj import name
# print(name)


# define main in python
 
# def abcdef() :
#     print("neosjfaleji")

# if __name__ == '__main__': #* defind main like this in python
#     print("nice")
#     abcdef()

'''
    if you define any main function then driven only 
    that function. that time global command not intrapreted
    by python intreprater
'''
#* code for create a random number
# import numpy as py
# ran = py.random.randint(32,323)
# print(ran)

#* join function
# deb = ["deb","raj","das","bappy"]
# a = ", ".join(deb)
# print(a,"other name")

#* Map function
# lis = ["2","32","43"]
# general method for convert string to int of lis element
# for i in range(len(lis)):
#     lis[i] = int(lis[i])
# map function through same work
# lis = list(map(int, lis))
# print(lis[1])

# other example of map function where we squar the element of list
# num = [3 ,2 ,6, 4 ,11 ,13]
# num = list(map(lambda x:x*x ,num))  # inside of map use lambda function
# for item in num:
#     print(item)

# Example 

# def sq(x):
#     return x*x
# def cude(x):
#     return x*x*x

# fun = [sq , cude]
# n = int(input("Enter n :: "))
# for i in range(n):
#     print(list(map(lambda x:x(i+1),fun)))

#* filter function example
# list_1 = [24 ,35,32,56,8,33,22,66,44,2,44,78]
# list_1 = list(filter(lambda x:x>35,list_1))
# print(list_1)

#* reduce function example
# from functools import reduce
# num = [1 , 3 , 3 , 5 ]
## general method for sum of the element of num list
# sum = 0 
# for i in num:
#     sum+=i
# print(sum)
## using reduce function
# num = reduce(lambda x,y:x+y, num)
# print(num)

#* Decorators in python

# def fun():
#     print("My name is Debraj Das")
# print(fun)
# poin_fun = fun 
# del fun # it delet the fun pointer but address store into poin_fun so poin_fun function work
# poin_fun()

# print(poin_fun)

#~ this function return the address of other function
# def fun(x):
#     if(x%2):
#         return print
#     else:
#         return pow

# a = fun(2)(2,3)
# if(a!=None):
#     print(a)
#~ pass the argument of other function
# def exe(fun):
#     fun(4)

# exe(print)

def deb(fun1):
    print("Exectution of deb function")
    def raj():
        print("executing start")
        fun1()
        print("execution is finish")
    return raj

# fun =deb(print)
# print("neos")
# fun()

@deb    #~ this call is Decorators in python this line very importance line so play with it
def das():
    print("My name is Debraj Das")

das()

# var = deb(das)    ## if () is join then raj function is called

# var()