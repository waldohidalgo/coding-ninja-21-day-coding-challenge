import math

def countDigits(n: int) -> int:
    # Write your code here
    return math.floor(math.log10(n))+1

print(countDigits(38))