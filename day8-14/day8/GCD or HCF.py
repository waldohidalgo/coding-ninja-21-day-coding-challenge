def calcGCD(n:int, m: int) -> int:
    # Write your code here
    a=min(n,m)
    b=max(n,m)
    while a!=0:
        rem=b%a
        b=a
        a=rem
    return b
    
print(calcGCD(9,0))