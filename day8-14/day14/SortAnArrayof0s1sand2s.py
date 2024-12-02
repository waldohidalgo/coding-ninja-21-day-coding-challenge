from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr, n):

    # Write your code here
    count1=0
    for i in range(n):
        if arr[i]!=0:
            count1+=1
        else:
            arr[i],arr[i-count1]=arr[i-count1],arr[i]
    count2=0
    for i in range(n-count1,n):
        if arr[i]==2:
            count2+=1
        else:
            arr[i],arr[i-count2]=arr[i-count2],arr[i]

#arr=[2, 2, 2, 2, 0, 0, 1, 0]
arr=[2,2,2,2,1,1,1,1,1,1,0]
sortArray(arr,len(arr))
print(arr)            