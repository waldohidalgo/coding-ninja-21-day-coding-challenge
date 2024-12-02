from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    #   Write your code here
    n=len(arr)
    carry=1
    for i in range(n-1,-1,-1):
        arr[i]+=carry
        carry=arr[i]//10
        arr[i]%=10

    if carry:
        arr.insert(0,carry)
    
    while arr[0]==0:
        arr.pop(0)
    

# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     print(addOneToNumber(arr))
arr=[9,9]
addOneToNumber(arr)
print(arr)