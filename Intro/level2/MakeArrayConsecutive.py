"""
Because the constraints include that the input array values are 
distinct, we can assume that once we find the min and max we can 
derive the number of values missing to make the input array 
contiguous

Therefore we can do this in linear time
"""

def solution(statues):
    if len(statues) == 1: return 0
    
    # find min & max
    local_min, local_max = statues[0],statues[0]
    
    cnt = 0
    
    for statue in statues:
        if statue > local_max:
            local_max = statue
        elif statue < local_min:
            local_min = statue
        else:
           cnt += 1
    
    return (local_max - local_min + 1) - len(statues)

