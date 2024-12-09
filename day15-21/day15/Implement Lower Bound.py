from typing import List

def lowerBound(arr: List[int], n: int, x: int) -> int:
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

arr=[1,1,1,1,1,2,2,2,2,2]
n=len(arr)
x=2
print(lowerBound(arr,n,x))
