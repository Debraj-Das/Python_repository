'''
Python is a script language, so you can run it directly.
so it is not necessary to compile it.
so it is like another script language, such as Cmd or Bash.

 This Note use for learn and practise python.

'''

import sys
import os
import math

sys.setrecursionlimit(100000000)
def inp(): return int(input())
def strng(): return input().strip()


def jn(x, l): return x.join(map(str, l))
def strl(): return list(input().strip())


def mul(): return map(int, input().strip().split())
def mulf(): return map(float, input().strip().split())
def seq(): return list(map(int, input().strip().split()))


def ceil(x): return int(x) if (x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if (x % d == 0) else x//d+1

# Code for Every test case


def solve():
    pass
    print("Hello world")


# print(__name__) # it will print __main__ if it is run directly or print the file name if it is imported


# main function
if __name__ == "__main__":
    t = 1
    # t = inp()
    for i in range(t):
        solve()
