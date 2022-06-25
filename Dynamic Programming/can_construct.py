def can_construct(target, words):
    if target == '':
        return True
    
    for word in words:
        if target[:len(word)] == word:
            if can_construct(target[len(word):], words):
                return True
    
    return False


def can_construct_memo(target, words, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    
    for word in words:
        if target[:len(word)] == word:
            res = can_construct_memo(target[len(word):], words)
            memo[target] = res
            if res:
                return True
    
    memo[target] = False
    return False


def can_construct_tab(target, words):
    length = len(target)
    tab = [False for _ in range(length+1)]
    tab[0] = True

    for i in range(length+1):
        if tab[i]:
            for word in words:
                if target[i:len(word)+i] == word:
                    try:
                        tab[i+len(word)] = True
                    except IndexError:
                        pass
    
    return tab[length]



cases = [
    ['', ['a', 'b']],
    ['a', ['a', 'b']],
    ['c', ['a', 'b']],
    ['abcd', ['abc', 'a', 'cd', 'b', 'abcd', 'c', 'd', 'ab', 'bc', 'abcd']],
    ['abcd', ['ab', 'yuy', 'fgfhh', 'bc', 'a', 'hgh']],
    ['abc', ['b', 'ab', 'abc', 'c', 'a', 'bc']],
    ['eeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeef']]
]

for case in cases:
    print(can_construct(*case))
    print(can_construct_memo(*case))
    print(can_construct_tab(*case))
    print()
