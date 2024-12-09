from typing import *

def spiralMatrix(matrix : List[List[int]]) -> List[int]:
    # Write your code here.
    i,j=0,0
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    directionIndex=0
    m,n=len(matrix),len(matrix[0])
    arr=[n,m]
    res=[]
    while all(arr):
        for r in range(2):
            for c in range(arr[r]):
                res.append(matrix[i][j])
                if c<arr[r]-1:
                    i,j=i+directions[directionIndex][0],j+directions[directionIndex][1]
                else:
                    directionIndex=(directionIndex+1)%4
                    i,j=i+directions[directionIndex][0],j+directions[directionIndex][1]
            arr[(r+1)%2]-=1
    return res

def spiralMatrix2(matrix : List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        res.extend(matrix[top][left:right + 1])
        top += 1
        res.extend(matrix[row][right] for row in range(top, bottom + 1))
        right -= 1
        if top <= bottom:
            res.extend(matrix[bottom][col] for col in range(right, left - 1, -1))
            bottom -= 1
        if left <= right:
            res.extend(matrix[row][left] for row in range(bottom, top - 1, -1))
            left += 1
    return res

def spiralMatrix3(matrix : List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    m,n=len(matrix),len(matrix[0])
    res = []
    cs,ce=0,n-1
    rs,re=0,m-1
    count=0
    while count<(m*n):
        for i in range(cs,ce+1):
            if count==(m*n):
                return res
            res.append(matrix[rs][i]) 
            count+=1
        rs+=1
        for i in range(rs,re+1):
            if count==(m*n):
                return res            
            res.append(matrix[i][ce])
            count+=1
        ce-=1
        for i in range(ce,cs-1,-1):
            if count==(m*n):
                return res            
            res.append(matrix[re][i])
            count+=1
        re-=1
        for i in range(re,rs-1,-1):
            if count==(m*n):
                return res            
            res.append(matrix[i][cs])
            count+=1
        cs+=1
    return res



arr=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# print(spiralMatrix(arr))
# print(spiralMatrix2(arr))
print(spiralMatrix3(arr))
#print(arr[2][2:-1:-1])