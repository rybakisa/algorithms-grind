from typing import List

DEBUG = True


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allowed_numbers = [i for i in range(1, n+1)]
        combination = []
        result = []

        deep = 0

        self.get_combination(k, allowed_numbers, combination, result, deep)
        return result


    def get_combination(self, k, allowed_numbers, combination, result, deep):
        deep += 1
        self.print('start', allowed_numbers, combination, result, deep)

        while allowed_numbers:
            num = allowed_numbers.pop()

            new_combination = combination.copy()
            new_combination.append(num)

            self.print('pop', allowed_numbers, new_combination, result, deep)

            if len(new_combination) < k:
                self.get_combination(k, allowed_numbers.copy(), new_combination, result, deep)
            elif len(new_combination) == k:
                result.append(new_combination)
            else:
                self.print('wtf', allowed_numbers, combination, result, deep)
                return
        
        self.print('end', allowed_numbers, combination, result, deep)
            

    def print(self, text, allowed_numbers, combination, result, deep):
        if not DEBUG:
            return

        buf = ''
        for _ in range(deep):
            buf += '='
        print(buf, text, deep)
        print(buf, allowed_numbers)
        print(buf, combination)
        print(buf, result)



class Solution_2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        allowed_numbers = [i for i in range(1, n+1)]
        result = []

        self.get_combination(k, allowed_numbers, [], result)
        return result


    def get_combination(self, k, allowed_numbers, combination, result):
        while allowed_numbers:
            num = allowed_numbers.pop()
            combination.append(num)

            if len(combination) < k:
                self.get_combination(k, allowed_numbers.copy(), combination, result)
            elif len(combination) == k:
                result.append(combination.copy())
                
            combination.pop()


class Solution_3():
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n==k:
            return [list(range(1,n+1))]
        if k==1:
            return [[i] for i in range(1,n+1)]
        
        one = self.combine(n-1,k)
        two = [i + [n] for i in self.combine(n-1, k-1)]
        return one + two


print(Solution_3().combine(7, 5))
