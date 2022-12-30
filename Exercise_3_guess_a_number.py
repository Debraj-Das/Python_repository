n = 18 
i = 0 
print("Enter the number for right guess in 9 chance.")
while i<9 :
    ip = int(input("Enter the guess :: "))
    if(ip<n) :
        print("enter number smaller than guess.")
    elif(ip>n) :
        print("enter number bigger than guess.")
    else :
        print("congulatialtion!,you gave right guess in ",(i+1)," no of guesses.")
        break
    i = i +1
if(i>=9) :
    print("Game over!")