# class Student : # as convension first letter of class is big letter
#     no_of_exam = 8
#     pass

# deb = Student()
# deb.cgp = 8.75
# deb.sem = 4
# print(deb.cgp,deb.sem,deb.no_of_exam)  # cgp and sem are object's instant variables not Class variable


# raj = Student()
# raj.father = "Chandra Sekhar Das"
# raj.no_of_exam = 9
# print(raj.father,raj.no_of_exam)

# print("no of exam in Student class :",Student.no_of_exam)
# print("deb attribute ",deb.__dict__)
# print("Student attribute ",Student.__dict__)

# Lec -- 56 to 
class Student :
    no_of_student = 0

    def __init__(self,name,roll_no,phone) -> None:
        self.name=name
        self.roll_no = roll_no
        self.phone = phone
        Student.no_of_student+=1
    
    @classmethod
    def from_dash(cls,string):
        #  arr = string.split(" ")
        #  return cls(arr[0],arr[1],arr[2])
        return cls(*string.split(" ")) # one line code of above code part
    
    @staticmethod           # Static variable
    def helloPrint():
        print("Hello world")

    def details(self):
        print("name :",self.name,"\nroll no :",self.roll_no,"\nPhone no :",self.phone)

    @classmethod    # class method for access class element form object
    def change(cls,no):
        print("no : ",Student.no_of_student)
        cls.no_of_student = no 
        print("no : ",Student.no_of_student)


# deb = Student("Debraj Das","21ME30078","9339573945") # intially by __init__ method(constructor)
deb = Student.from_dash("Debraj 21ME30078 9339573945")   # intially by Class method

sou = Student("Soumik nayak","21ME10070","024792875")

deb.details()

sou.change(5)

print("no of student : ",Student.no_of_student)

deb.details()
print(f"\n{sou.no_of_student} and {deb.no_of_student}")

deb.helloPrint()


