"""
I am so sorry for the horror which I am about to introduce you to
OOF, 19/20 tests passed
"""
def solution(a, b):
    
    for i in range(0,len(a)):
        if a[i] == b[i]:
            continue
        else:
            for j in range(i+1,len(a)):
                if a[j] == b[j]:
                    continue
                elif a[j] == b[i] and a[i] == b[j]:
                    # assume to do the swap in a
                    aj = a[j]
                    a[j] = b[i]
                    b[i] = aj
                    
                    ai = a[i]
                    a[i] = b[j]
                    b[j] = ai
                else:
                    return False
    return True

"""
This is the solution I ended up using

increment a count, and collect the not good items 
"""
def solution(a, b):
    count = 0
    list_a = []
    list_b = []
    for i in range(len(a)):
        if (a[i]!= b[i]):
            count +=1
            list_a.append(a[i])
            list_b.append(b[i])

    if (count ==0):
        return True 

    elif count ==2: 
        return set(list_a)==set(list_b)

    else:
        return False