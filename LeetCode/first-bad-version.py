FIRST_BAD = 14

def isBadVersion(n: int) -> bool:
    return n >= FIRST_BAD



def firstBadVersion_2checks(n: int) -> int:
    min, max = 0, n

    while min <= max:
        current = (max + min) // 2

        if isBadVersion(current):
            # check previous
            if isBadVersion(current - 1):
                # two bad versions
                # need to check prev versions
                max = current - 2
            else:
                return current
                
        else:
            # check next
            if isBadVersion(current + 1):
                return current + 1
            else:
                # two good versions
                # need to check further versions
                min = current + 2


def firstBadVersion(n: int) -> int:
    min, max = 1, n

    while min < max:
        current = (min + max) // 2

        if isBadVersion(current):
            max = current
        else:
            min = current + 1
    
    return max



cases = [
    123,
    132532,
    444444444444,
]
for num in cases:
    print('Answer: ', firstBadVersion(num))
    print('Answer: ', firstBadVersion_2checks(num))
    print()
