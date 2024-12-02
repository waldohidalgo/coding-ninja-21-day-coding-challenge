from typing import List


def getSecondOrderElements(n: int,  a: List[int]) -> List[int]:
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

#a=[1, 2, 3, 4, 5]
#a=[3,4,5,2]
a=[4,5,3,6,7]
print(getSecondOrderElements(len(a),a))
