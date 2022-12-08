"""
Really think out edge cases, in this case being able to accomodate one odd represented character as the middle character is necessary
"""
def solution(inputString):
    from collections import Counter
    middlechar_used = False
    for key, value in Counter(inputString).items():
        if value % 2 != 0 and middlechar_used:
            return False
        elif value % 2 != 0 and not middlechar_used:
            middlechar_used = True
        elif value % 2 != 0:
            return False
    return True
