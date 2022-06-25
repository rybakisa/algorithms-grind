from typing import List

def search(nums: List[int], target: int) -> int:
    step = middle_index = len(nums) // 2

    while (step > 0):
        step = step // 2 

        print(step, middle_index, nums[middle_index])

        if target > nums[middle_index]:     
            middle_index += step
        elif target < nums[middle_index]:
            middle_index -= step
        else:
            return middle_index
    return -1


def search_2(nums: List[int], target: int) -> int:
    min = 0
    max = len(nums) - 1

    while(min<=max):
        index = (min + max) // 2
        check = nums[index]

        print(min, max, index, nums[index])

        if target > check:
            min = index + 1
        elif target < check:
            max = index - 1
        else:
            return index
    return -1


a = [-1,0,1,3,5,9,12,13,14,17,44,456,500,501,502,503,504,505,999]
target = 999
print('Answer: ', search(a, target))
print('Answer: ', search_2(a, target))
