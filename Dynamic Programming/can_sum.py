
def can_sum(sum, array, memo={}):
    if sum == 0: return True
    if sum < 0: return False
    if memo.get(sum, None) is not None: return memo[sum]

    for num in array:
        sum -= num
        if can_sum(sum - num, array, memo):
            memo[sum] = True
            return True
    
    memo[sum] = False
    return False


def can_sum_tab(sum, array):
    tab_array = [False for _ in range(sum + 1)]
    tab_array[0] = True

    for i in range(sum + 1):
        if tab_array[i]:
            for num in array:
                try:
                    tab_array[i + num] = True
                except IndexError:
                    pass
    print(tab_array)
    return tab_array[-1]


cases = [
    [10, [1, 2, 3, 4, 5]],
]

for case in cases:
    # print(all_sums(*case))
    print()
    print(can_sum(*case))
    print()
    print(can_sum_tab(*case))