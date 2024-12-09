from collections import *
from math import *

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    res=[[1]]
    for i in range(1,n):
        res.append([1]+[res[i-1][j]+res[i-1][j-1] for j in range(1,i)]+[1])
    return res

print(printPascal(2))