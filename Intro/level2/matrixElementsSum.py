def solution(matrix):
    # iterate over array of arrays
    # maintain defaultdict of indices which are below haunted rooms
    # for a row in matrix
        # if a room is free
            # add it to the haunted dict
        # elif room index isn't in haunted dict
            # add it to the sum
    
    import collections
    haunted_rooms = collections.defaultdict(bool)
    cnt = 0
    for floor in matrix:
        for i,room in enumerate(floor):
            if room == 0:
                haunted_rooms[i] = True
            elif not haunted_rooms[i]:
                cnt += room
    return cnt