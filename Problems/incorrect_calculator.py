
print("\nHello everyone, my name is Debraj Das.")
print("Good morning, nice to meet all of you.")
print("now, I start today coding work.\n")

#* exercise 2 
a = int(input("Enter the first number :: "))
opr = input("Enter the operator :: ")
b = int(input("Enter the second number :: "))
if((a==45) and (b==3) and (opr=="*")) :
    print(a,opr,b," = ",555)
elif ((a==45) and (b == 9) and (opr == "+")) :
    print(a , opr , b , " = ",77)
elif ((a == 56) and (b == 6) and (opr == "/")) :
    print(a , opr ,b , " = ",4)
else :
    if(opr == "+") :
        print(a , opr , b , " = ", a+b)
    elif(opr == "-") :
        print(a , opr , b , " = ",a-b)
    elif(opr == "*") :
        print(a , opr , b , " = ",a*b)
    else :
        print(a , opr , b , " = ",a/b)
    