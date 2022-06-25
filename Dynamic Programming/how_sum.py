
def how_sum(sum, array, memo={}):
    if sum in memo:
        return memo[sum]
    if sum == 0:
        return []
    if sum < 0:
        return None

    for num in array:
        res = how_sum(sum - num, array, memo)
        if res is not None:
            memo[sum] = res + [num]
            return memo[sum]

    memo[sum] = None
    return None


def how_sum_tab(sum, array):
    tab_array = [None for _ in range(sum + 1)]
    tab_array[0] = []

    for i in range(sum + 1):
        if tab_array[i] is not None:
            for num in array:
                try:
                    if tab_array[i + num] is None:
                        tab_array[i + num] = tab_array[i] + [num]
                except IndexError:
                    pass
    
    # print(tab_array)
    return tab_array[-1]


cases = [
    [100, [3, 5, 20, 10, 1]],
]

for case in cases:
    print(how_sum(*case))
    print()
    print(how_sum_tab(*case))
