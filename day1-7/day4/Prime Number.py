import math

def isPrime(n:int) -> bool:
    # Write your code here
    if n==1:
        return "YES"
    root=int(math.sqrt(n))
    val="YES"
    for i in range(2,root+1):
        if n%i==0:
            val="NO"
            break
    return val


print(isPrime(1))