"""
Use a counter to keep up with the moves used
Run from index 1 until the end
If the current index is less than the last, update the value at the index and count

Note, this doesn't have to be contiguous. I inferred that it had to be and wasted some time :(

"""
def solution(inputArray):
    moves = 0
    for i in range(1,len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            #moves to increase to one number greater than previous
            moves += inputArray[i-1] - inputArray[i] + 1
            #modify current to previous plus one
            inputArray[i] = inputArray[i-1] + 1
    return moves