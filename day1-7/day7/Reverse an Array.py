from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    for i in range(n//2):
        nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
    return nums

n=6
nums= [5, 7, 8, 1, 6, 3]
print(reverseArray(n,nums))