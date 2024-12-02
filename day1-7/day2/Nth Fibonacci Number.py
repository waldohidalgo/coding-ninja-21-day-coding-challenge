from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=6
arr=[1]*(n+1)
for i in range(3,n+1):
    arr[i]=arr[i-1]+arr[i-2]
print(arr[n])