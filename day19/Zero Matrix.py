from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    # Write your code here.
    if n<=1 or m<=1:
        return matrix
    
    first_row_have_zero=any(matrix[0][j]==0 for j in range(m))
    first_col_have_zero=any(matrix[i][0]==0 for i in range(n))

    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]==0:
                matrix[0][j]=0
                matrix[i][0]=0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j]=0
    if first_row_have_zero:
        for j in range(m):
            matrix[0][j]=0
    if first_col_have_zero:
        for i in range(n):
            matrix[i][0]=0

matrix=[[2,3,0,5]]
n=len(matrix)
m=len(matrix[0])
zeroMatrix(matrix,n,m)
print(matrix)