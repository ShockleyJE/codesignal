def solution(inputString):
    spl=inputString.split('.')
    if len(spl) != 4: return False
    
    #print(spl)
    for i,d in enumerate(spl):
        print(f"i {i} d {d}")

        if not d: return False
        
        if re.findall('[a-z]+', d): return False
                
        if len(d) > 1 and d[0] == '0': return False
        
        if not int(d) <= 255 or not int(d) >= 0:
            return False
    
    return True
