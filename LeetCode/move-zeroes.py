from typing import List

def moveZeroes_1(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # insert_index = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(i))
    
    print(nums)


def moveZeroes_2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def swap(nums, swap_from, swap_to):
        nums[swap_from] = nums[swap_to]
        nums[swap_to] = 0


    swap_from = 0
    swap_to = 1
    print('> ', swap_from, swap_to)

    while swap_to < len(nums) and swap_to < len(nums):
        if nums[swap_from] == 0 and nums[swap_to] != 0:
            swap(nums, swap_from, swap_to)
            swap_from += 1
            swap_to += 1
        elif nums[swap_from] == 0 and nums[swap_to] == 0:
            swap_to += 1
        elif nums[swap_from] != 0 and nums[swap_to] != 0:
            swap_from += 2
            swap_to += 2
        elif nums[swap_from] != 0 and nums[swap_to] == 0:
            swap_from += 1
            swap_to += 1
        
        print('> ', nums)
        print('> ', swap_from, swap_to)
    
    print(nums)


nums = [1,0,0,0,0,1,1,1,6,0,8,5,5,0]
print(nums)
# moveZeroes_1(nums.copy())
moveZeroes_2(nums.copy())
