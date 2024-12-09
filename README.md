# 21-Day Coding Challenge: Ninja Slayground 2.0

Repositorio con el código solución a los 21 desafíos diarios.

## Tabla de Contenido

- [21-Day Coding Challenge: Ninja Slayground 2.0](#21-day-coding-challenge-ninja-slayground-20)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Certificados Obtenidos](#certificados-obtenidos)
    - [Certificado Participación](#certificado-participación)
    - [Certificado Level 1: 7 days Streak](#certificado-level-1-7-days-streak)
    - [Certificado Level 2: 14 days Streak](#certificado-level-2-14-days-streak)
    - [Certificado Level 3: 21 days Streak](#certificado-level-3-21-days-streak)
  - [Ejercicios Resueltos](#ejercicios-resueltos)
    - [Day 1: Switch Case statement](#day-1-switch-case-statement)
    - [Day 2: Nth Fibonacci Number](#day-2-nth-fibonacci-number)
    - [Day 3: Number of digits](#day-3-number-of-digits)
    - [Day 4: Prime Number](#day-4-prime-number)
    - [Day 5: Check Sorted Array](#day-5-check-sorted-array)
    - [Day 6: Reverse a Number](#day-6-reverse-a-number)
    - [Day 7: Reverse an Array](#day-7-reverse-an-array)
    - [Day 8: GCD or HCF](#day-8-gcd-or-hcf)
    - [Day 9: Second Largest Number](#day-9-second-largest-number)
    - [Day 10: Highest / Lowest Frequency Elements](#day-10-highest--lowest-frequency-elements)
    - [Day 11: Two Sum](#day-11-two-sum)
    - [Day 12: Add One To Number](#day-12-add-one-to-number)
    - [Day 13: Binary Search](#day-13-binary-search)
    - [Day 14: Sort An Array of 0s, 1s and 2s](#day-14-sort-an-array-of-0s-1s-and-2s)
    - [Day 15: Implement Lower Bound](#day-15-implement-lower-bound)
    - [Day 16: Valid Parentheses](#day-16-valid-parentheses)
    - [Day 17: Implement Upper Bound](#day-17-implement-upper-bound)
    - [Day 18: Spiral Matrix](#day-18-spiral-matrix)
    - [Day 19: Zero Matrix](#day-19-zero-matrix)
    - [Day 20: Pascal's Triangle](#day-20-pascals-triangle)
    - [Day 21: Number of Inversions](#day-21-number-of-inversions)

## Certificados Obtenidos

### Certificado Participación

![Certificado Participación](./certificados/certificado_participacion.webp)

### Certificado Level 1: 7 days Streak

![Certificado Level 1: 7 days Streak](./certificados/certificado_level1.webp)

### Certificado Level 2: 14 days Streak

![Certificado Level 2: 14 days Streak](./certificados/certificado_level2.webp)

### Certificado Level 3: 21 days Streak

![Certificado Level 3: 21 days Streak](./certificados/certificado_level3.webp)

## Ejercicios Resueltos

### Day 1: Switch Case statement

In a menu-driven program, the user is given a set of choices of things to do (the menu) and then is asked to select a menu item.

There are 2 choices in the menu:

Choice 1 is to find the area of a circle having radius 'r'.

Choice 2 is to find the area of a rectangle having dimensions 'l' and 'b'.

You are given the choice 'ch' and an array 'a'.

If ‘ch’ is 1, ‘a’ contains a single number ‘r’. If ‘ch’ is 2, ‘a’ contains 2 numbers, ‘l’ and ‘b’.

Consider the choice and print the appropriate area.

```py
from typing import *
from math import pi
def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    if ch == 1:
        return round(pi*a[0]**2,5)
    elif ch == 2:
        return f'{a[0] * a[1]:.5f}'
    else:
        return -1
```

### Day 2: Nth Fibonacci Number

The n-th term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula:

    F(n) = F(n - 1) + F(n - 2),
    Where, F(1) = 1, F(2) = 1

Provided 'n' you have to find out the n-th Fibonacci Number. Handle edges cases like when 'n' = 1 or 'n' = 2 by using conditionals like if else and return what's expected.

"Indexing is start from 1"

```py
n=int(input())
arr=[1]*(n+1)
for i in range(3,n+1):
    arr[i]=arr[i-1]+arr[i-2]
print(arr[n])
```

### Day 3: Number of digits

You are given a number 'n'.
Return number of digits in ‘n’.

```py
import math

def countDigits(n: int) -> int:
    # Write your code here
    return math.floor(math.log10(n))+1
```

### Day 4: Prime Number

A prime number is a positive integer that is divisible by exactly 2 integers, 1 and the number itself.

You are given a number 'n'.

Find out whether 'n' is prime or not.

```py
def isPrime(n:int) -> bool:
    # Write your code here
    if n==1:
        return False
    root=int(n**0.5)
    for i in range(2,root+1):
        if n%i==0:
            return False
    return True
```

### Day 5: Check Sorted Array

You have been given an array ‘a’ of ‘n’ non-negative integers.You have to check whether the given array is sorted in the non-decreasing order or not.

Your task is to return 1 if the given array is sorted. Else, return 0.

Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: 1

The given array is sorted in non-decreasing order; hence the answer will be 1.

```py
def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    for i in range(1,n):
        if a[i]<a[i-1]:
            return 0
    return 1
```

### Day 6: Reverse a Number

You are given a number 'n'.

Return an integer that is the reverse of ‘n’.

Note:
Reverse of ‘n’ means an integer where, the most significant digit of ‘n’ is the least significant digit of the number, the second most significant digit of ‘n’ is the second least significant digit of the number and so on.

```py
from typing import List

def reverseNumber(n: int) -> int:
    # Write your code here
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
```

### Day 7: Reverse an Array

Given an array 'arr' of size 'n'.

Return an array with all the elements placed in reverse order.

Note:
You don’t need to print anything. Just implement the given function.

```py
from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    for i in range(n//2):
        nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
    return nums
```

### Day 8: GCD or HCF

You are given two integers 'n', and 'm'.

Calculate 'gcd(n,m)', without using library functions.

Note:
The greatest common divisor (gcd) of two numbers 'n' and 'm' is the largest positive number that divides both 'n' and 'm' without leaving a remainder.

```py
def calcGDC(n:int, m: int) -> int:
    # Write your code here
    a=min(n,m)
    b=max(n,m)
    while a!=0:
        rem=b%a
        b=a
        a=rem
    return b
```

### Day 9: Second Largest Number

You have been given an array ‘a’ of ‘n’ unique non-negative integers.

Find the second largest and second smallest element from the array.

Return the two elements (second largest and second smallest) as another array of size 2.

```py
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    n=len(a)
    pmax,smax=float('-inf'),float('-inf')
    pmin,smin=float('inf'),float('inf')

    for i in range(n):
        if a[i]>pmax:
            smax=pmax
            pmax=a[i]
        elif a[i]<pmax and a[i]>smax:
            smax=a[i]

        if a[i]<pmin:
            smin=pmin
            pmin=a[i]
        elif a[i]>pmin and a[i]<smin:
            smin=a[i]
    return [smax,smin]
```

### Day 10: Highest / Lowest Frequency Elements

Given an array 'v' of 'n' numbers.

Your task is to find and return the highest and lowest frequency elements.

If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element.

```py
from typing import List
from collections import Counter
def getFrequencies(v: List[int]) -> List[int]:
    # Write your code here
    freq = Counter(v)

    min_val,min_freq=float('inf'),float('inf')
    max_val,max_freq=0,0
    for val,fq in freq.items():
        if fq==min_freq and val<min_val:
            min_val=val
        if fq<min_freq:
            min_freq,min_val=fq,val

        if fq==max_freq and val<max_val:
            max_val=val
        if fq>max_freq:
            max_freq,max_val=fq,val


    return [max_val,min_val]
```

### Day 11: Two Sum

Sam want to read exactly ‘TARGET’ number of pages.

He has an array ‘BOOK’ containing the number of pages for ‘N’ books.

Return YES/NO, if it is possible for him to read any 2 books and he can meet his ‘TARGET’ number of pages.

Example:
Input: ‘N’ = 5, ‘TARGET’ = 5
‘BOOK’ = [4, 1, 2, 3, 1]

Output: YES
Explanation:
Sam can buy 4 pages book and 1 page book.

```py
def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    seen=set()
    for num in book:
        if target-num in seen:
            return "YES"
        seen.add(num)
    return "NO"
```

### Day 12: Add One To Number

Given a non-negative number represented as an array of digits, you have to add 1 to the number, i.e, increment the given number by one.

The digits are stored such that the most significant digit is at the starting of the array and the least significant digit is at the end of the array.

For Example
If the given array is {1,5,2}, the returned array should be {1,5,3}.

Note:

Input array can contain leading zeros, but the output array should not contain any leading zeros (even if the input array contains leading zeroes).
For Example:
If the given array is {0,2}, the returned array should be {3}.

```py
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
```

### Day 13: Binary Search

You are given an integer array 'A' of size 'N', sorted in non-decreasing order. You are also given an integer 'target'. Your task is to write a function to search for 'target' in the array 'A'. If it exists, return its index in 0-based indexing. If 'target' is not present in the array 'A', return -1.

Note:
You must write an algorithm whose time complexity is O(LogN)

```py
def search(nums: [int], target: int):
    # write your code logic !!
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

### Day 14: Sort An Array of 0s, 1s and 2s

You have been given an array/list 'arr' consisting of 'n' elements.

Each element in the array is either 0, 1 or 2.

Sort this array/list in increasing order.

Do not make a new array/list. Make changes in the given array/list.

Example :
Input: 'arr' = [2, 2, 2, 2, 0, 0, 1, 0]

Output: Final 'arr' = [0, 0, 0, 1, 2, 2, 2, 2]

Explanation: The array is sorted in increasing order.

```py
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
```

### Day 15: Implement Lower Bound

You are given an array 'arr' sorted in non-decreasing order and a number 'x'. You must return the index of the lower bound of 'x'.

Note:

1. For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'.If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.

2. Try to do this in O(log(n)).

Example:
Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0

Output: 0

Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.

```py
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    l=0
    r=n-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==x and (arr[mid-1]<x if mid>0 else True):
            return mid
        elif arr[mid]>=x:
            r=mid-1
        else:
            l=mid+1
    return l
```

### Day 16: Valid Parentheses

You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .

Return true if the given string 'S' is balanced, else return false.

For example:
'S' = "{}()".

There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
So the 'S' is Balanced.

```py
def isValidParenthesis(s: str) -> bool:
    # Write your code here
    stack=[]
    for c in s:
        if c=='(' or c=='[' or c=='{':
            stack.append(c)
        elif c==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
        elif c==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                return False
        elif c=='}':
            if stack and stack[-1]=='{':
                stack.pop()
            else:
                return False
    return not stack
```

### Day 17: Implement Upper Bound

You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.Implement the ‘upper bound’ function to find the index of the upper bound of 'x' in the array.

Note:

1. The upper bound in a sorted array is the index of the first value that is greater than a given value.
2. If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
3. Try to write a solution that runs in log(n) time complexity.

Example:

Input : ‘arr’ = {2,4,6,7} and ‘x’ = 5,

Output: 2

Explanation: The upper bound of 5 is 6 in the given array, which is at index 2 (0-indexed).

```py
from typing import List

def upperBound(arr: List[int], x: int, n: int) -> int:
    # Write your code here.
    l,r=0,n-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==x and (arr[mid+1]>x if mid<n-1 else True):
            return mid+1
        elif arr[mid]>x:
            r=mid-1
        else:
            l=mid+1
    return l
```

### Day 18: Spiral Matrix

You are given a 2D matrix ‘MATRIX’ of ‘N’\*’M’ dimension. You have to return the spiral traversal of the matrix.

Example:

Input:
MATRIX = [ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60] ]
Output:
1 3 5 7 20 60 34 30 23 10 11 16

Explanation: Starting from the element in the first row and the first column, traverse from left to right (1 3 5 7), then top to bottom (20 60), then right to left (34 30 23), then bottom to up (10) and then left to right (11 16).

```py
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
```

### Day 19: Zero Matrix

You are given a matrix 'MATRIX' of dimension 'N' x 'M'. Your task is to make all the elements of row 'i' and column 'j' equal to 0 if any element in the ith row or jth column of the matrix is 0.

Note:

1. The number of rows should be at least 1.

2. The number of columns should be at least 1.

```py
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
```

### Day 20: Pascal's Triangle

You are given an integer N. Your task is to return a 2-D ArrayList containing the pascal’s triangle till the row N.

A Pascal's triangle is a triangular array constructed by summing adjacent elements in preceding rows. Pascal's triangle contains the values of the binomial coefficient.

```py
def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    res=[[1]]
    for i in range(1,n):
        res.append([1]+[res[i-1][j]+res[i-1][j-1] for j in range(1,i)]+[1])
    return res
```

### Day 21: Number of Inversions

There is an integer array ‘A’ of size ‘N’.

Number of inversions in an array can be defined as the number of pairs of ‘i’, ‘j’ such that ‘i’ < ‘j’ and ‘A[i]’ > ‘A[j]’.

You must return the number of inversions in the array.

For example,
Input:
A = [5, 3, 2, 1, 4], N = 5
Output:
7
Explanation:
The pairs satisfying the condition for inversion are (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), and (3, 4).
The number of inversions in the array is 7.

```py
from typing import *

class Solution:
    def mergeSort(self,arr,low,high):
        count_inversion=0
        if low<high:
            mid=(low+high)//2
            count_inversion+=self.mergeSort(arr,low,mid)
            count_inversion+=self.mergeSort(arr,mid+1,high)
            count_inversion+=self.merge(arr,low,mid,high)
        return count_inversion
    def merge(self,arr,low,mid,high):
        count_inversion=0
        temp=[0]*(high-low+1)
        i=low
        j=mid+1
        k=0
        while i<=mid and j<=high:
            if arr[i]<=arr[j]:
                temp[k]=arr[i]
                k+=1
                i+=1
            else:
                temp[k]=arr[j]
                k+=1
                j+=1
                count_inversion+=mid-i+1 #se agrega la inversion
        while i<=mid:
            temp[k]=arr[i]
            k+=1
            i+=1
        while j<=high:
            temp[k]=arr[j]
            k+=1
            j+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]
        return count_inversion
def numberOfInversions(a : List[int], n : int) -> int:
    # Write your code here.
    return Solution().mergeSort(a,0,n-1)
```
