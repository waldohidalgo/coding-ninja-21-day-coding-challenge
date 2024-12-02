from typing import *

def isSorted(n: int,  a: List[int]) -> int:
    # Write your code here.
    for i in range(1,n):
        if a[i]<a[i-1]:
            return 0
    return 1
