from operator import neg
from readline import write_history_file
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    sorted_squares = []
    negatives_queue = []
    
    for num in nums:
        squared_num = num**2
        if num <= 0:
            negatives_queue.insert(0, squared_num)
        else:
            if negatives_queue:
                while negatives_queue and squared_num >= negatives_queue[0]:
                    sorted_squares.append(negatives_queue.pop(0))
            sorted_squares.append(squared_num)

    return sorted_squares + negatives_queue


def sortedSquares2(nums: List[int]) -> List[int]:
    sorted_squares = []

    while len(nums) >= 2:
        first = abs(nums[0])
        last = abs(nums[len(nums)-1])

        if first > last:
            sorted_squares.insert(0, nums.pop(0)**2)
        else:
            sorted_squares.insert(0, nums.pop()**2)

    if nums:
        sorted_squares.insert(0, nums[0]**2)

    return sorted_squares


def sortedSquares3(nums: List[int]) -> List[int]:
    first = 0
    last = len(nums) - 1
    sorted_squares = []

    while first <= last:
        if abs(nums[first]) > abs(nums[last]): 
            sorted_squares.insert(0, nums[first]**2)
            first += 1
        else:
            sorted_squares.insert(0, nums[last]**2)
            last -= 1

    return sorted_squares


def sortedSquares4(nums: List[int]) -> List[int]:
    return sorted([n*n for n in nums])



nums = [-7,-3,-2,0,1,2]
print(sortedSquares(nums.copy()))
print(sortedSquares2(nums.copy()))
print(sortedSquares3(nums.copy()))
print()
print(sortedSquares4(nums.copy()))
