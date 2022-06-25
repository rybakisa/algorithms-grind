FIRST_BAD = 44444
NUMBER = 132532

def isBadVersion(n: int) -> bool:
    return n >= FIRST_BAD


def firstBadVersion(n: int) -> int:
    min = 0
    max = n
    current = n // 2
    
    while min <= max:
        print(min, max, current)
        if isBadVersion(current):
            # check previous
            if isBadVersion(current - 1):
                # two bad versions
                # need to check prev versions
                max = current - 2
                print('bb')
            else:
                print('gb')
                return current
                
        else:
            # check next
            if isBadVersion(current + 1):
                print('gb')
                return current + 1
            else:
                # two good versions
                # need to check further versions
                print('gg')
                min = current + 2
        current = (max + min) // 2


print(
    'Answer: ', firstBadVersion(NUMBER)
)