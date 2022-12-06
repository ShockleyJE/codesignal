def solution(inputArray):
    def calcmaxd(currmax, e1, e2):
        thismaxd = max(e1,e2) - min(e1,e2)
        return max(currmax, thismaxd)
    
    maxd=0
    for i,val in enumerate(inputArray):
        if i == 0:continue
        print(f"calling cmaxd {maxd}, {val}, {inputArray[i-1]}")
        maxd = calcmaxd(maxd, val, inputArray[i-1])
        
    return maxd

