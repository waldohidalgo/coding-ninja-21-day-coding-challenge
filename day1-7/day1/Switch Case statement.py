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

print(areaSwitchCase(2, [3, 2]))