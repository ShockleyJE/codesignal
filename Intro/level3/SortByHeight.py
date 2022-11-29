"""
-1 is the key to indicate a value represents a  nonperson tree which will not be sorted
"""
def solution(a):
    nontree = list(filter(lambda x: x != -1, a))
    nontree.sort()
    
    return list(map(lambda x: x if x == -1 else nontree.pop(0), a ))