def solution(inputArray):
    if len(inputArray) == 2: return inputArray[0] * inputArray[1]
    
    cmax = inputArray[0] * inputArray[1]
    last_idx = 0
    
    for i in range(1,len(inputArray)):
        n = inputArray[i]
        if inputArray[last_idx] * n > cmax:
            cmax = inputArray[last_idx] * n 
        last_idx = i
        
    return cmax