num1 = input("Enter the first number :: ")
num2 = input("Enter the second number :: ")

try :                                          #* it is syntex of Try Except Exception Handling in python.
    print("The sum of these two number is ",int(num1)+int(num2))
except Exception as error :
    print(error)

print("This line is improtance.")