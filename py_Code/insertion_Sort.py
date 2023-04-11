import sys
import os
import math
if os.environ.get('ONLINE_JUDGE') == None:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

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
def insertion_sort(arr):
    i = 0
    n = len(arr)
    while (i < n):
        j = i
        while (j and arr[j - 1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        i += 1


def solve():
    arr = seq()
    insertion_sort(arr)
    for i in arr:
        print(i,end= ' ')



# main function
if __name__ == "__main__":
    t = 1
    # t = inp()
    for i in range(t):
        solve()
