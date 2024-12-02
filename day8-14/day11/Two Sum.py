from typing import List

def read(n: int, book: List[int], target: int) -> str:
    # Write your code here.

    seen=set()
    for num in book:
        if target-num in seen:
            return "YES"
        seen.add(num)
    return "NO"

book=[1,2]
target=1
print(read(len(book),book,target))