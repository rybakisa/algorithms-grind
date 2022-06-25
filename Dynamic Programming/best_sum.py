def all_sums(sum, array, answers=[], path=[]):
    for num in array:
        new_sum = sum - num

        if new_sum == 0:
            answers.append(path + [num])
        elif new_sum > 0:
            all_sums(new_sum, array, answers, path + [num])
        
    return answers


def best_sum(sum, array, min_path=[], path=[], memo={}):
    if sum in memo and len(memo[sum]) <= len(path):
        # print('hehe')
        return min_path
    else:
        # print(memo)
        memo[sum] = path

    for num in array:
        new_sum = sum - num

        if (new_sum == 0
        and (
            len(min_path) == 0 
            or len(min_path) > len(path) + 1)
        ):
            min_path = path + [num]
        elif new_sum > 0:
            min_path = best_sum(new_sum, array, min_path, path + [num], memo)

    return min_path


def best_sum_2(sum, array, memo={}):
    if sum in memo:
        # print('hehe')
        return memo[sum]
    if sum == 0:
        return []
    if sum < 0:
        return None

    shortest_path = None
    
    for num in array:
        new_sum = sum - num
        path = best_sum_2(new_sum, array)

        if path is not None:
            new_path = path + [num]
            if (shortest_path is None 
            or (len(shortest_path) > len(new_path) 
            and len(shortest_path) >= 0)):
                shortest_path = new_path

    memo[sum] = shortest_path
    # print(memo)
    return shortest_path


def best_sum_tab(sum, array):
    tab_array = [None for _ in range(sum + 1)]
    tab_array[0] = []

    for i in range(sum + 1):
        if tab_array[i] is not None:
            for num in array:
                try:
                    # if tab_array[i + num] is None or len(tab_array[i + num]) > len(tab_array[i]) + 1:
                    if tab_array[i + num] is None:
                        tab_array[i + num] = tab_array[i] + [num]
                except IndexError:
                    pass
    
    # print(tab_array)
    return tab_array[-1]



cases = [
    [100, [2, 3, 4, 5]],
]

for case in cases:
    # print(all_sums(*case))
    print()
    print(best_sum(*case))
    print()
    print(best_sum_2(*case))
    print()
    print(best_sum_tab(*case))
