def count_construct(target, words):
    if target == '':
        return 1
    
    count = 0
    for word in words:
        if target[:len(word)] == word:
            count += count_construct(target[len(word):], words)

    return count


def count_construct_memo(target, words, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    
    count = 0
    for word in words:
        if target[:len(word)] == word:
            count += count_construct_memo(target[len(word):], words)

    memo[target] = count
    return count


def count_construct_tab(target, words):
    length = len(target)
    tab = [0 for _ in range(length+1)]
    tab[0] = 1

    for i in range(length+1):
        # print(tab)
        if tab[i]:
            # print(i, tab[i])
            for word in words:
                # print(target[i:len(word)+i], word)
                if target[i:len(word)+i] == word:
                    try:
                        tab[i+len(word)] += tab[i]
                        # print('[+]', i+len(word), tab[i+len(word)])
                    except IndexError:
                        pass
        # print('--------------')
    
    return tab[length]



cases = [
    # ['', ['a', 'b']],
    # ['a', ['a', 'b']],
    # ['c', ['a', 'b']],
    # ['abcd', ['abc', 'a', 'cd', 'b', 'abcd', 'c', 'd', 'ab', 'bc', 'abcd']],
    # ['abcd', ['ab', 'yuy', 'fgfhh', 'bc', 'a', 'hgh']],
    # ['abc', ['b', 'ab', 'abc', 'c', 'a', 'bc']],
    ['eeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeef']]
]

for case in cases:
    print(count_construct(*case))
    print(count_construct_memo(*case))
    print(count_construct_tab(*case))
    print()