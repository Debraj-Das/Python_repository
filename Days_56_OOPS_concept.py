# import sys
# import os
# import math
# if os.environ.get('ONLINE_JUDGE') == None:
#     sys.stdin = open('input.txt', 'r')

'''
#* Day 56 of 100 days of Code
## Introduction to OOPs in python
# OOPs stands for Object Oriented Programming
# Introduction to Object-Oriented Programming in Python: In programming languages, mainly there are two approaches that are used to write program or code.
#                   1). Procedural Programming
#                   2). Object-Oriented Programming
# The procedure we are following till now is the “Procedural Programming” approach. So, in this session, we will learn about Object Oriented Programming (OOP). The basic idea of object-oriented programming (OOP) in Python is to use classes and objects to represent real-world concepts and entities.
# A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have. Properties are the data or state of an object, and methods are the actions or behaviors that an object can perform.
# An object is an instance of a class, and it contains its own data and methods. For example, you could create a class called "Person" that has properties such as name and age, and methods such as speak() and walk(). Each instance of the Person class would be a unique object with its own name and age, but they would all have the same methods to speak and walk.
# One of the key features of OOP in Python is encapsulation, which means that the internal state of an object is hidden and can only be accessed or modified through the object's methods. This helps to protect the object's data and prevent it from being modified in unexpected ways.
# Another key feature of OOP in Python is inheritance, which allows new classes to be created that inherit the properties and methods of an existing class. This allows for code reuse and makes it easy to create new classes that have similar functionality to existing classes.
# Polymorphism is also supported in Python, which means that objects of different classes can be treated as if they were objects of a common class. This allows for greater flexibility in code and makes it easier to write code that can work with multiple types of objects.
# In summary, OOP in Python allows developers to model real-world concepts and entities using classes and objects, encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism.

#* This Program is for pratice and write of objective oriention example small concept
    # Some importance point -->
    # 1. Try to always attribute as a private member of class
    # 2. And accordingly create property function for all those attributes
    # 3. For any attribute which type of property function, it can be rw or r- or -w (read - r) and (write - w)


    # Proper Structure of Class -->
    # class
    #     private :
    #         Personal Attribute not Inherited Attribute  (which is not inherited from the parent class attribute)

    #     protected :
    #         1. Inherited Attribute (which is inherited from the parent class attribute)
    #         2. Internal Function (which is used for the internal work of the class)

    #     public :
    #         Methods -->
    #             Constructor -> 1. nonparameter 2. parameter 3. copy
    #             mutator (assign value and change value of the attribute)(getter)
    #             Accessor (get value of the attribute)(setter)
    #             Facilitator (do some work with the attribute and return value )
    #             Enquiry (check some condition and return value)
    #             Destructor (destroy the object of the class)


#* Day 57 of 100 days of Code
# classes and objects in python
# creating a class
class Person:
    # creating a class attribute
    name = "Debraj"
    age = 20 
    income = 100000
    # creating a method
    def info(self):
        print("Name is ", self.name)
        print("Age is ", self.age)
        print("Income is ", self.income)

# creating an object
obj1 = Person()
obj1.age = 21
obj1.info()

# in class there are many components e.g. class name, class attribute, class method, object, object attribute, object method, etc.


# * Day 58 of 100 days of Code
# constructor in python
# there are two types of constructor in python
# 1. parameterized constructor 2. default constructor

# parameterized constructor


class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group


obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

# default constructor


class Details:
    def __init__(self):
        print("animal Crab belongs to Crustaceans group")


obj1 = Details()

# constaructor is a special type of method which is used to initialize the instance members of the class.
# constructor is called automatically when the object is created.
# This constructor can be parameterized or default or default argument constructor.


class Person:
    name = "Debraj"
    age = 20
    # this is a default constructor with default value

    def __init__(self, name="Debraj", age=20) -> None:
        self.name = name
        self.age = age
        print(f"{self.name} and {self.age}")

    def info(self):
        print(f"{self.name} is {self.age} years old.")


obj1 = Person()
obj1.info()
obj2 = Person("soumik", 19)
obj2.info()


# * Day 59 of 100 days of Code
# Decorators in python


# it defines the extra functionality to an existing function without changing the structure of the function.
# it is use as decorators in python.
# geet is a decorator function which take a function as a parameter and return a function after adding some extra functionality to it.
def geet(fx):
    def mfx():
        print("Hello", end=' ')
        fx()
        print("Welcome to python")
    return mfx


@geet   # this is a decorator
def hello():
    print("Debraj")


@geet
def welcome():
    print("Soumik")


hello()
print('\n')
welcome()

# it is like --> geet(hello)()

def name():
    print("Debraj")

print('\n')
new = geet(name)
new()

import logging
# print(logging.basicConfig(level=logging.INFO))
## I didn't understand the logging module and log_function_call decorator
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

print(my_function(1, 2))


#* Day 60 of 100 days of Code
# Getter and Setter in python
class MyClass:
    __nam = "Debraj"
    def __init__(self, value):
        self._value = value
        self.__nam = "Soumik"
   
    @property   # this is a decorator which is used to access the value of the variable(getter)
    def value(self):
        return self._value
    
    @property
    def nam(self):
        return self.__nam

    @value.setter   # this is a decorator which is used to set the value of the variable(setter)
    def value(self, new_value):
        self._value = new_value

obj = MyClass(10)
print(obj.nam)
print("Previous vaule : ",obj.value)
obj.value = 20
print("Update vaule : ",obj.value)

# __ is used to make the variable private and _ is used to make the variable protected. 


# * Day 61 of 100 days of Code
# Inheritance in python
# syntax -->
# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):  # this is a derived class and Employee is a base class
    def showLanguage(self):
        print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()

# Single Inheritance
# Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.

class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child(Parent):
    def func2(self):
        print("This function is in child class.")


object = Child()
object.func1()
object.func2()

# Multiple Inheritance
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.

class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)


class Father:
    fathername = ""

    def father(self):
        print(self.fathername)


class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother :", self.mothername)


s1 = Son()
s1.fathername = "Mommy"
s1.mothername = "Daddy"
s1.parents()

# Multi-level Inheritance
# In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.

class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

# Hierarchical Inheritance
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.

class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")


class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

# Hybrid Inheritance
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
# in this example Inheritance is multiple and multilevel both
class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


object = Student3()
object.func1()
object.func2()



# * Day 62 of 100 days of Code
# Access Modifiers in python
# In python there are not any access modifiers like public, private, protected.
# But we can use _ and __ to make the variable protected and private respectively.


class Student:
    def __init__(self):
        self._name = "Harry"    # protected variable
        self.__roll = 12    # private variable

    def _funName(self):      # protected method
        return "CodeWithHarry"


class Subject(Student):  # inherited class
    pass


obj = Student()
obj1 = Subject()
# print(dir(obj))    # this will print all the methods and variables of the class

# calling by object of Student class
# print(obj.__roll)       # this will give an error
print(obj._Student__roll)  # this will print the value of the private variable __roll
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
# print(obj1.__roll)  # this will give an error
print(obj1._Student__roll)  # this will print the value of the private variable __roll

#~ public access modifier
# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)

#~ private access modifier
# By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.
# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
# Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.
class Student: 
    def __init__(self, age, name): 
        self.__age = age      # An indication of private variable
        
        def __funName(self):  # An indication of private function
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Student(21,"Harry")
obj1 = Subject

# calling by object of class Student
print(obj.__age)
print(obj.__funName())

# calling by object  of class Subject
print(obj1.__age)
print(obj1.__funName())

#~ Name Mangling in Python
# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.
# In the example above, the attribute _nonmangled_attribute is marked as nonmangled by convention, but can still be accessed from outside the class. The attribute __mangled_attribute is private and its name is "mangled" to _MyClass__mangled_attribute, so it can't be accessed directly from outside the class, but you can access it by calling _MyClass__mangled_attribute

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

#~ protected access modifier
# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.
# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())


# * Day 63 of 100 days of Code
# Solution of Exercise 5
# Done

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




#* Day 65 of 100 days of Code
# static method in python
# A static method is a method that knows nothing about the class or instance it was called on. 
# It just gets the arguments that were passed, no implicit first argument. 
# It is basically useless in Python -- you can just use a module function instead of a static method.

class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self, n):
    self.num = self.num +n
    
  @staticmethod
  def add(a, b):    # static method
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7, 2)) 


# * Day 66 of 100 days of Code
# Instance variable and class variable
# Instance variable is the variable which is defined inside the constructor of the class or object as object_name.variable_name
# class variable is the variable which is defined outside the constructor of the class but inside of class


class Employee:
    companyName = "Apple"  # class variable
    noOfEmployees = 0

    def __init__(self, name):
        self.name = name    # instance variable
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(
            f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")


# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3 # accessing instance variable
emp1.companyName = "Apple India"    # create a new instance variable and assign value
emp1.showDetails()
Employee.companyName = "Google" # accessing class variable
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle" # create a new instance variable and assign value
emp2.showDetails()

#* Day 67 of 100 days of Code
# solution of exercise 6 (Done) 

#* Day 68 of 100 days of Code
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
  


# * Day 69 of 100 days of Code
# Class method in python
# A class method is a method that is bound to a class rather than its object or instance.
# It doesn't require creation of a class instance, much like staticmethod.


class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod    # class method decorator , it convert the method into class method
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)


# * Day 70 of 100 days of Code
# Class method as a alternative constructor in python


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size):
        return cls(size, size)
    
    def area(self):
        return self.width * self.height


rectangle = Rectangle.square(10)
print(rectangle.area())

# another example as person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
    @property
    def details(self):
        print(f'The name is {self.name} and age is {self.age}')

person = Person.from_string("John Doe, 30")
person.details


#* Day 71 of 100 days of Code
# dir , __dict__ and , help , __doc__ in python
import os
print(dir(os))  # it gives all the attributes and methods of the module as list
print('\n')
print(os.__dict__) # it gives all the attributes and methods of the module as dictionary
print('\n')
print(help(os)) # it gives the documentation of the module and it give all the attributes and methods of the module
print('\n')
print(os.__doc__) # it gives the documentation of the module as string and it give docstring of the module

l = dir(os)
for i in l:
    print(i)

print(os.truncate.__doc__) # it gives the documentation of the truncate method of the os module
print(help(os))

# it is used to get the documentation of the class for understanding the class and module


#* Day 72 of 100 days of Code
# Super() function in python
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)


# * Day 73 of 100 days of Code
# Magic methods(dunder methods) in python
# some magic method e.g - __init__ , __len__ , __call__ , __str__ , __repr__  etc.
from typing import Any


class Person:
    def __init__(self) -> None:  # __init__ is a magic method
        self.name = "Debraj Das"
        self.age = 25

    def __len__(self): # it is used to get the length of the object
        return len(self.name)

    def __str__(self): # it is used to print the object
        return f"The name is {self.name} and age is {self.age}"

    def __call__(self, *args: Any, **kwds: Any) -> Any: # it is used to call the object as function
        print("Calling... the person class")
    
    def __repr__(self) -> str:  # it is used to represent the object
        return f"Person('{self.name}', {self.age})"
    
    def display(self):  # it is used to display the object and it is not a magic method
        print(f"{self.name} is {self.age} years old")
    
    
p1 = Person()   # creating the object of the class
p1()    # calling the object as function
print(p1)   # printing the object
print(repr(p1)) # representing the object
print(len(p1))  # getting the length of the object
p1.display()    # displaying the object


# * Day 74 of 100 days of Code
# Method Override in python

class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("Area :", end=' ')
        return self.dim1*self.dim2
# Driver class
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius , radius)
        self.pi = 3.14159 # pi value
    
    def area(self): # method override
        return super().area() * self.pi # calling the area method of the parent class by super() method

c = Circle(5)
print(c.area())

#* Day 75 of 100 days of Code
# Excersice 7 : Solution of Clear the Clutter

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

# Done the Excersice 8


#* Day 77 of 100 days of Code
# Operator Overloading in python
# Operator overloading means giving extended meaning beyond their predefined operational meaning.
# some e.g of operator overloading are + , - , * , / , // , % , ** , < , > , <= , >= , == , != , [] , () , @ , etc.
# Operator overloading is also known as magic methods or dunder methods. so it use magic method for operator overloading.
# some example of magic methods are __add__ + , __sub__  - , __mul__ * , __truediv__ /  
# __floordiv__ // , __mod__ | | , __pow__ ** 
# __lt__ < , __gt__ > , __le__ <= , __ge__ >= , __eq__ == , __ne__ != 
# __getitem__ [] , __call__ () , etc.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y) # prints 4, 6

'''

