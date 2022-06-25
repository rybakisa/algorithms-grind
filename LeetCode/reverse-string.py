from typing import List

def swap(s, a, b):
    if s[a] == s[b]:
        pass

    temp = s[a]
    s[a] = s[b]
    s[b] = temp


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    lenght = len(s)
    for i in range(lenght//2):
        swap(s, i, lenght - i - 1)
    
    print(s)


def reverseString_2(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s = s[::-1]
    print(s)



s = ['s', 'o', 's', 'i', 'b', 'i', 'b', 'u', '1']
reverseString(s.copy())
reverseString_2(s.copy())