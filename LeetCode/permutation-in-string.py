class Solution:
    def permutation_exists(self, window, etalon):
        for char in window:
            if char in etalon:
                etalon.remove(char)
            else:
                return False
        return True
            

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        window_size = len(s1)
        window = list(s2[:window_size])
        etalon = list(s1)
        for i in range(window_size, len(s2)):
            if self.permutation_exists(window, etalon.copy()):
                return True
            window[i%window_size] = s2[i]
        
        return self.permutation_exists(window, etalon)


class Solution_2:
    def checkSymbol(self, symbol, etalon):
        try:
            etalon.remove(symbol)
            return True
        except ValueError:
            return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        window_size = len(s1)

        i = 0
        found = False
        etalon = list(s1)

        while i+window_size-1 < len(s2):
            print(f'Checking window {s2[i:i+window_size]}')
            if len(etalon) < len(s1):
                etalon = list(s1)

            found = True
            for j in range(window_size):
                print(f'checking s2[{i+window_size-1-j}]={s2[i+window_size-1-j]}')
                print(etalon)

                if self.checkSymbol(s2[i+window_size-1-j], etalon):
                    print('[+] found')
                    pass
                else:
                    print('[+] not found, move window')
                    i = i + window_size - j
                    found = False
                    break
                    
            if found:
                break

        return found

        

s1 = "abc"
s2 = "cccccbabbbaaaa"

print(
    Solution_2().checkInclusion(s1, s2)
)
