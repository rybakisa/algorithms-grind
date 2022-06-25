def reverse_word(s, start, end):
    res = s[start:end]
    res = res[::-1]
    return res

def reverseWords(s: str) -> str:
    length = len(s)
    last_word_start = 0
    reversed = ''

    for current_char in range(length):
        if s[current_char] == ' ':
            reversed = reversed + reverse_word(s, last_word_start, current_char) + ' '
            last_word_start = current_char + 1
        elif current_char == length - 1:
            reversed = reversed + reverse_word(s, last_word_start, current_char + 1) 
    
    return reversed


s = "Let's take LeetCode contest"
print(s)
print(reverseWords(s))
