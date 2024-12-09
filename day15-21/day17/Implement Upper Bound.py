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

#arr=[1,5,5,7,7,9,10]
#x=5
# arr=[1,2,5,6,10]
# x=10
arr=[1,4,7,8,10]
x=7
n=len(arr)
print(upperBound(arr,x,n))