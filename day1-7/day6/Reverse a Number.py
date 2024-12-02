from typing import List

def reverseNumber(n: int) -> int: 
    # Write your code here
    
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev

sol=reverseNumber(0)
print(sol)