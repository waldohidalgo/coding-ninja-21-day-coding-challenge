from typing import List
from collections import Counter
def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    freq = Counter(v)

    min_val,min_freq=float('inf'),float('inf')
    max_val,max_freq=0,0
    for val,fq in freq.items():
        if fq==min_freq and val<min_val:
            min_val=val
        if fq<min_freq:
            min_freq,min_val=fq,val

        if fq==max_freq and val<max_val:
            max_val=val
        if fq>max_freq:
            max_freq,max_val=fq,val


    return [max_val,min_val]

arr= [1, 2, 3, 1, 1, 4]
#arr=[10,10,10,3,3,3]
print(getFrequencies(arr))