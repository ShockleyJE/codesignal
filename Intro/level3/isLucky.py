"""
My approach was correct, however I got tricked up on the end inclusivity of string slicing 
and the functools reduce syntax for Python
"""

def solution(n):
    
    strn = str(n)
    if len(strn) %2 != 0: return False
    
    fh = strn[:math.floor(len(strn)/2)]
    sh = strn[math.ceil((len(strn)-1)/2):]
    
    from functools import reduce
    if reduce(lambda curr, acc: int(acc) + int(curr), fh) == reduce(lambda curr, acc: int(acc) + int(curr), sh):
        return True
    else:
        return False
