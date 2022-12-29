import random
print("****Best of luck for Guess game****\nThis is the game of Guess number[1,3000] and only 10 oppertunity\n")
n = 0 
num = random.randint(1, 3000)
while (n<10):
    print(n+1,"Enter the number ::",end=' ')
    guss = int(input())
    if(guss==num):
        print("\n*****you are correct congulatulation...*****")
        break
    elif(guss<num):
        print("\tBigger then ",guss,'\n')
    else:
        print("\tSmaller then ",guss,'\n')
    n+=1
        
if(n==10):
    print("Best of luck for next time")
    print("The number is",num)
