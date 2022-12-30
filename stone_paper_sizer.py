import random

print("This game is stone- paper - sizer ***")
print("For input \n\tstone : s")
print("\tpaper : p")
print("\tsizer : c")

n = int(input("How many you want to play :: "))
comp = 0 
you = 0 
opion = [1,2,3]

for i in range(n):
    #* user choice time
    print(f"{i+1} ) your choice (s p c) ::",end=' ')
    y_op = input()
    if(y_op=='s' or y_op=='S'):
        num = 1
    elif(y_op=='p' or y_op=='P'):
        num = 2
    elif(y_op=='c' or y_op=='C'):
        num = 3
    else:
        print("You enter wrong input")
        continue
    #* print the computer option
    op_com = random.choice(opion)
    if(op_com==1):
        print("Computer : s")
    elif(op_com==2):
        print("Computer : p")
    elif(op_com==3):
        print("Computer : c")
    #* Compera the both option
    if((op_com*num) == 3):
        if(op_com>num):
            you+=1
            print("you win")
        else:
            comp+=1
            print("you lose")
    else:
        if(op_com<num):
            you+=1
            print("you win")
        elif(op_com>num):
            comp+=1
            print("you lose")
        else:
            print("Tye")

## final result time
print("\n Now match is over :: ")
print("you score is ",you,"and computer score",comp)
if(you>comp):
    print("you win finally. so congratulation")
elif(comp>you):
    print("Computer win and for best of luck for next time")
else:
    print("Match is TYE")

