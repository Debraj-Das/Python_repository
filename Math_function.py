from math import *

# it take a string as input and return the string as result

def sum(s):
    sum = 0
    for i in s.split(' '):
        sum += int(i)
    s = s.replace(' ', '+')
    s = f"{s} = {sum}"
    return s

def sub(s):
    l = s.split(' ')
    ret = int(l[0]) - int(l[1]) 
    s = f"{l[0]} - {l[1]} = {ret}"
    return s

def mul(s):
    l = s.split(' ')
    mul = 1 
    for i in l:
        mul *= int(i)
    s = s.replace(' ', '*')
    s = f"{s} = {mul}"
    return s

def div(s):
    l = s.split(' ')
    if(int(l[1]) != 0):
        ret = int(l[0]) / int(l[1]) 
        s = f"{l[0]} / {l[1]} = {ret}"
    else:
        s = "Error: Division by zero"
    return s

def pow(s):
    l = s.split(' ')
    ret = int(l[0]) ** int(l[1]) 
    s = f"{l[0]} ^ {l[1]} = {ret}"
    return s

def sqrt(s):
    l = s.split(' ')
    ret = sqrt(int(l[0]))
    s = f"sqrt({l[0]}) = {ret}"
    return s

def log(s):
    l = s.split(' ')
    ret = log(int(l[0]), int(l[1]))
    s = f"log({l[0]}) = {ret}"
    return s
