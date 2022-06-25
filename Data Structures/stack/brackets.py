OPENINGS = ['(', '[', '{']
CLOSINGS = [')', ']', '}']

def brackets_match(opening, closing):
    return OPENINGS.index(opening) == CLOSINGS.index(closing)

def is_valid(equasion):
    stack = []

    for bracket in equasion:
        if bracket in OPENINGS:
            stack.append(bracket)

        elif bracket in CLOSINGS:
            try:
                opening = stack.pop()
            except IndexError:
                return False

            if not brackets_match(opening=opening, closing=bracket):
                return False

        else:
            return False

    return len(stack) == 0


tests = [
    '()',
    '(]',
    '(()',
    '())',
    '([{}])',
    '([{]})',
    '(){}[]',
    '([]{})',
    '([(]{})',
    '{()[]}([][]())',
    '{()[]}([][](a))',
]

for test in tests:
    print(test, is_valid(test))
