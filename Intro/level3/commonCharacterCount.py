"""
The goal is to find the count of shared characters between two strings
What made this a little tricky was that it needs to be constrained to the number of instances of a common character 
between the two strings
if s1 has two a's and s2 has three a's then you can only count two

Counter big O is nlogn. This could have been sped up with a different implementation but its ezpz

"""

def solution(s1, s2):
    s1_set, s2_set = set(s1), set(s2)
    common_chars = s1_set.intersection(s2_set)
    shrd_cntr = 0
    import collections
    from collections import Counter
    s1_ctr = collections.Counter(s1)
    s2_ctr = collections.Counter(s2)
    for cc in common_chars:
        shrd_cntr += min(s1_ctr[cc], s2_ctr[cc])
    return shrd_cntr