n = int(input("Enter a number :: "))
ch = int(input("Enter 0 or 1 :: "))
if(ch):
    i = 1
    while(i<=n):
        print(i*'*')
        i+=1
else:
    i = n
    while(i):
        print(i*'*')
        i-=1
