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

    def __add__(self, other):   # __add__ is a magic method for + operator
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y) # prints 4, 6


#* Day 78 of 100 days of Code
# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Cat(Animal):  # Cat class inherits the Animal class(Single inheritance example)
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
        
    def make_sound(self):
        print("Meow!")

d = Cat("Catman", "Doggerman")
d.make_sound()

a = Animal("Catman", "Cat")
a.make_sound()


#* Day 79 of 100 days of Code
# Multiple inheritance is a type of inheritance where a class inherits properties and behaviors from more than one parent class.
class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()    # it prints the show method of the Employee class because the Employee class is inherited first
print(DancerEmployee.mro())  # mro() is used to print the order of the class in which the class is inherited
# it prints 1. DancerEmployee 2. Employee 3. Dancer 4. Object(All the classes are inherited from the object class)


#* Day 80 of 100 days of Code
# Multilevel inheritance is a type of inheritance where a class inherits properties and behaviors from a parent class and also from the parent of the parent class.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        super().__init__(name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")
        
dog = GoldenRetriever("Max", "Golden")
dog.show_details()
print(GoldenRetriever.mro())


#* Day 81 of 100 days of Code
# Hybrid and Hierarchical Inheritance
# Hybrid Inheritance is a combination of multiple and multilevel inheritance.
# Hierarchical Inheritance is a type of inheritance where a class inherits properties and behaviors from more than one child class.

# Example of Hybrid Inheritance 
class BaseClass:
  pass

class Derived1(BaseClass):
  pass  

class Derived2(BaseClass):
  pass  

class Derived3(Derived1, Derived2):
  pass

# Hierarchical Inheritance
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass


#* Day 82 of 100 days of Code
# Solution of Exercise 8 : Merge PDFs
# Done


#* Day 83 of 100 days of Code
# Exercise 9 : Shoutout in Python
# Write a python program to shoutout to your friends in python using the win32com module.
import win32com.client

# Calling the Dispatch method of the module which interact with Microsoft Speech SDK to speak the given input from list

speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["Debraj", "praveen" , "Aditya" , "Rahul" , "Raj"]

for i in l:
    speaker.Speak(f"Shoutout to {i}")



#* Day 84 of 100 days of Code
import time
def usingWhile():
    i = 0
    sum = 0
    while i<50000:
        sum = sum + i
        i = i +1
    print("sum is : ",sum)



def usingFor():
    sum = 0
    for i in range(50000):
        sum = sum + i
    print("sum is : ",sum)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)


print(4)
time.sleep(3)
print("This is printed after 3 seconds")
 
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time) 


#* Day 85 of 100 days of Code
# command line utility using python
# Download files from the internet using python
import argparse
import requests

def download_file(url, local_filename): 
  if local_filename is None:
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
  with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              # If you have chunk encoded response uncomment if
              # and set chunk_size parameter to None.
              #if chunk: 
              f.write(chunk)
  return local_filename
  
parser = argparse.ArgumentParser()  

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
# print(args.url)
# print(args.output, type(args.output))
# print(args)   # it prints the namespace of the arguments
download_file(args.url, args.output)    # it downloads the file from the url and saves it with the name given in the output argument


# Delet the jpg files from the current directory
import os , glob
l = glob.glob("*.jpg")
for i in l :
    os.remove(i)


#* Day 86 of 100 days of Code
# Walrus Operator in python
# Walrus operator is used to assign values to variables within an expression in places where assignment statements are not allowed, for example, in lambda expressions, conditional expressions, while loops, etc.
# Walrus operator is denoted by :=

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:  # it assigns the length of the list to the variable n and checks if it is greater than 0
    print(numbers.pop())


#* Day 87 of 100 days of Code
# Shutil module in python
# Shutil module is used to perform high-level file operations like copying and removal of files and folders.
import shutil
shutil.rmtree("__pycache__")   # it removes the folder and all the files inside it
# like this shutil has many functions like copyfile(), copy(), copytree(), move(), rmtree(), which are used to perform file operations
# link of the documentation of shutil module : https://docs.python.org/3/library/shutil.html


#* Day 88 of 100 days of Code
# Solution of Exercise 9 : Shoutout in Python
# Done

#* Day 89 of 100 days of Code
# Requests module in python
# Requests module is used to send HTTP requests to a server and get the response from the server.
# link of the documentation of requests module : https://docs.python-requests.org/en/master/
# import requests
# r = requests.get("https://www.google.com")
# print(r.text)   # it prints the html code of the google.com website

# import requests

# url = "https://api.example.com/login"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     "Content-Type": "application/json"
# }
# data = {
#     "username": "myusername",
#     "password": "mypassword"
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.text)

import requests 
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)


soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'harry',
#     "body": 'bhai',
#     "userId": 12,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)



#* Day 90 of 100 days of Code
# Exercise 10 : NewApi in python
# NewApi is used to get the data from the internet using python
# link of the documentation of NewApi : https://newsapi.org/docs/client-libraries/python



#* Day 91 of 100 days of Code
# Generators in python
# Generators are used to create iterators in python, they are written just like a normal function but they use yield keyword instead of return keyword
# Generators are used to save memory and time because of it create the values on the fly

def my_generate():
    for i in range(5):
        yield i  # it returns the value of i and saves the state of the function

gen = my_generate()     # it creates a generator object
for i in range(4):
    print(next(gen))


#* Day 92 of 100 days of code
# Function Caching in python
# Function caching is used to save the time of the program by saving the result of the function in the memory
# it is done by using lru_cache decorator from functools module
# it is used when we have to call the function again and again with the same arguments

import functools

@functools.lru_cache(maxsize=None)  # it saves the result of the function in the memory
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(60))
# Output: 6765

# By using this you can do very easily dynamic programming and memorisation in programming


#* Day 93 of 100 days of Code
# Exercise 10 : solution of NewApi in python
import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")


#* Day 94 of 100 days of Code
# Exercise 11 : Drink Water Notification in python
## this exercise Panding 


#* Day 95 of 100 days of Code
# Regular Expressions in python
# Regular Expressions are used to :
# find the patterns in the string , replacing the string and splitting the string and extracting the information from the string

import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']

new_text = re.sub(pattern, "dog", text)

print(new_text)
# Output: "The dog is in the dog."

## https://regexr.com/

pattern = r"[A-Z]+yclone"
text = # Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018.
Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. 
It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). 
As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, and became a post-tropical cyclone on 7 March
#    # Here # place used trple quotes because it is a multiline string

match = re.search(pattern, text) # it returns the first match of the pattern in the text
print(match)

# matches = re.finditer(pattern, text)
# for match in matches:
#   print(match.span()) 
#   print(text[match.span()[0]: match.span()[1]])


#* Day 96 of 100 days of Code
#@ Asyncio in python
# Asyncio is used to do the asynchronous programming in python and it is used to do the concurrent programming in python
# it is used to do the parallel programming in python and it is not block the main thread of the program

import asyncio

async def my_async_function():
    # asynchronous code here
    print("run the async function")
    await asyncio.sleep(1)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()  # it is used to run the single function
    print(result)
    L = await asyncio.gather(
        my_async_function(),    # it is used to run the multiple function at the same time
        my_async_function(),
        my_async_function(),
    )
    for i in L:
        print(i)
    

asyncio.run(main())

import time
import asyncio 
import requests


async def function1():
  print("func 1") 
  URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
  response = requests.get(URL)
  open("instagram1.jpg", "wb").write(response.content)
  return "Harry"
  
async def function2():
  print("func 2") 
  URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram2.jpg", "wb").write(response.content)
  return "Debraj"
  
async def function3():
  print("func 3")
  URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  response = requests.get(URL)
  open("instagram3.jpg", "wb").write(response.content)
  return "Das"

async def main():
  # await function1()
  # await function2()
  # await function3()
  # return 3
  L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
  print(L)
  # task = asyncio.create_task(function1())
  # # await function1()
  # await function2()
  # await function3()

asyncio.run(main())


#* Day 97 of 100 days of Code
#@ Multithreading in python
# Multithreading is used to do the concurrent programming in python and it is used to do the parallel programming in python
# it is very importance for the network programming and multiprocessing programming in python

import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)
  return seconds

def main():
    time1 = time.perf_counter()
    # Normal Code
    # func(4) 
    # func(2)
    # func(1)
    
    
    # Same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    # Calculating Time 
    time2 = time.perf_counter()
    print("time : ",time2 - time1)

# main()


def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func, 3)
    # future2 = executor.submit(func, 2)
    # future3 = executor.submit(func, 4)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)


poolingDemo()


#* Day 98 of 100 days of Code
# Multiprocessing in python
# Multiprocessing is used to do the concurrent programming in python and it is used to do the parallel programming in python

# import concurrent.futures
import multiprocessing
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 

if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(50):
    # downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

# with concurrent.futures.ProcessPoolExecutor() as executor:
#   l1 = [url for i in range(60)]
#   l2 = [i for i in range(60)]
#   results = executor.map(downloadFile, l1, l2)
#   for r in results:
#     print(r)


#* Day 99 of 100 days of Code
# Exercise 11 : Destop Notifier

## Work pending

#* Day 100 of 100 days of Code
# Conclution and Where to go from here
# congratulations for completing the 100 days of code challenge

# Conclusion
# Congratulations on completing the 100 days of Python code challenge! You have likely gained a solid foundation in the language and developed a range of skills, from basic syntax to more advanced concepts such as object-oriented programming.
# However, this is just the beginning of your journey with Python. There are many more topics to explore, including machine learning, web development, game development, and more.

# Where to go from here:
# To continue your learning journey, consider exploring the following resources:

# Python books: There are many excellent books on Python that can help you deepen your knowledge and skills. Some popular options include "Python Crash Course" by Eric Matthes, "Automate the Boring Stuff with Python" by Al Sweigart, and "Fluent Python" by Luciano Ramalho. I would also like to recommend "Hands on Machine Learning book by Aurélien Géron"

# YouTube Projects: There are many YouTube projects available which can be watched after you have some basic understanding of python

# Python communities: There are many online communities where you can connect with other Python learners and experts, ask questions, and share your knowledge. Some popular options include the Python subreddit, the Python Discord server, and the Python community on Stack Overflow.

# GitHub repositories: GitHub is a great resource for finding Python projects, libraries, and code snippets. Some useful repositories to check out include "awesome-python" (a curated list of Python resources), "scikit-learn" (a machine learning library), and "django" (a web development framework).

'''

# Link to some resources
# Tkinter - You can learn Tkinter which is used to create GUIs from here : https://www.cs.mcgill.ca/~hv/classes/MS/TkinterPres/#Overview
# Machine Learning - I loved this playlist from Google Developers    https://www.youtube.com/playlist?list=PLOU2XLYxmsIIuiBfYad6rFYQU_jL2ryal
# Django - For Django, try the tutorial from the official documentation. Trust me its really good   https://docs.djangoproject.com/en/4.1/intro/tutorial01/
# Overall, the key to mastering Python (or any programming language) is to keep practicing and experimenting. Set yourself challenges, work on personal projects, and stay curious. Good luck!

#? There are some Ideas where I have to work on 
# 1. Desktop Notifier
# Asyncio , multiprocessing, multithreading
# Regular Expression
# Web Scraping
# API using python
# GUI using python

