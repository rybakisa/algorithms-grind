class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_start_i = cur_lenght = max_lenght = 0
        char_mapping = {}
        
        for i in range(len(s)):
            char = s[i]

            # new substring concluded
            cur_position = char_mapping.get(char, None)
            if cur_position is not None \
            and cur_position >= substr_start_i:
                substr_start_i = char_mapping[char] + 1
            else:
                cur_lenght = i - substr_start_i + 1
                # fix new max lenght
                max_lenght = max(max_lenght, cur_lenght)

            char_mapping[char] = i

            # print(char, char_mapping)
            # print(i, start, cur_lenght, max_lenght)
            # print('---------')

        return max_lenght


s = '12312345123'
print(s)
print()
print(Solution().lengthOfLongestSubstring(s))