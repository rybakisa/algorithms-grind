from copy import deepcopy

def all_construct(target, words):
    if target == '':
        return [[]]
    
    combs = []
    for word in words:
        if target[:len(word)] == word:
            new_comb = all_construct(target[len(word):], words)
            for comb in new_comb:
                comb.append(word)

            combs += new_comb

    return combs


def all_construct_memo(target, words, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    
    combs = []
    for word in words:
        if target[:len(word)] == word:
            new_comb = deepcopy(all_construct_memo(target[len(word):], words, memo))
            for comb in new_comb:
                comb.append(word)
            combs += new_comb

    if target not in memo:
        memo[target] = combs
    return combs


def all_construct_tab(target, words):
    lenght = len(target)
    tab = [[] for i in range(lenght+1)]
    tab[0] = [[]]
    
    for i in range(lenght + 1):
        if tab[i] != []:
            for word in words:
                if target[i:len(word)+i] == word:
                    if i + len(word) < lenght + 1:
                        prev_combs = deepcopy(tab[i])
                        for comb in prev_combs:
                            comb.append(word)
                        tab[i+len(word)] += prev_combs

    return tab[lenght]



cases = [
    ['', ['a', 'b']],
    ['a', ['a', 'b']],
    ['c', ['a', 'b']],
    ['ab', ['a', 'b', 'ab']],
    ['abcd', ['abc', 'a', 'cd', 'b', 'abcd', 'c', 'd', 'ab', 'bc', 'abcd']],
    ['abcd', ['ab', 'yuy', 'fgfhh', 'bc', 'a', 'hgh']],
    ['abc', ['b', 'ab', 'abc', 'c', 'a', 'bc']],
    ['eeeeeeeeeeeeeeeeeeeeeeeeee', ['e', 'ee', 'eee', 'eeee', 'eeeef']]
]

for case in cases:
    print(all_construct(*case))
    print(all_construct_memo(*case))
    print(all_construct_tab(*case))
    print()
