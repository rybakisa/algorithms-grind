from sre_constants import IN
from typing import List

INPUT = [1,3,5,6]
TARGET = 2


def searchInsert(nums: List[int], target: int) -> int:
    min = 0
    mid = 0
    max = len(nums) - 1
    
    while min<=max:
        mid = (min + max) // 2
        print(min, mid, max)

        if target > nums[mid]:
            min = mid + 1
        elif target < nums[mid]:
            max = mid - 1
        else:
            return mid
    
    if target > nums[mid]:
        return mid + 1
    elif target < nums[mid]:
        return mid
    else:
        print('Something wrong')
        return -1


print(
    searchInsert(
        nums=INPUT,
        target=TARGET,
    )
)