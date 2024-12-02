from typing import List

def search(nums: List[int], target: int):
    # write your code logic !!
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

nums=[1,2,3,4,5,6,7]
target=9
print(search(nums,target))