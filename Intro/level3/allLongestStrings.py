"""
First tryyy

Approach, use a list def dict and create a frequency array, maintaining the key for the max

"""

def solution(inputArray):
    if len(inputArray) == 1: return inputArray
    
    import collections
    freqlist = collections.defaultdict(list)
    maxlen = 0
    
    for s in inputArray:
        freqlist[len(s)].append(s)
        if len(s) > maxlen: maxlen = len(s)
        
    return freqlist[maxlen]
