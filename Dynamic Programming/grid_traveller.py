def moves_count(x, y):
    if x == y == 1: return 1
    if x == 0 or y == 0: return 0

    return moves_count(x-1, y) + moves_count(x, y-1)


def moves_count_memo(x, y, memo={}):
    if (x, y) in memo: return memo[(x, y)]
    if x == y == 1: return 1
    if x == 0 or y == 0: return 0

    memo[(x, y)] = moves_count_memo(x-1, y, memo) + moves_count_memo(x, y-1, memo)
    return memo[(x, y)]


def moves_count_tab(x, y):
    if x == y == 1: return 1
    if x == 0 or y == 0: return 0

    tab = [[0 for _ in range(x+1)] for _ in range(y+1)]
    tab[1][1] = 1

    for col in range(1, y+1):
        for row in range(1, x+1):
            if col+1 <= y:
                tab[col+1][row] += tab[col][row]
            if row+1 <= x:
                tab[col][row+1] += tab[col][row]

    return tab[x][y]


cases = [
    [0, 0],
    [0, 1],
    [1, 1],
    [2, 2],
    [10, 10],
]

for case in cases:
    print(moves_count(*case))
    print(moves_count_memo(*case))
    print(moves_count_tab(*case))
    print()