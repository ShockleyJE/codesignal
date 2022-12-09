def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    yourMin = min(yourLeft, yourRight)
    yourMax = max(yourLeft, yourRight)
    friendsMin = min(friendsLeft, friendsRight)
    friendsMax = max(friendsLeft, friendsRight)
    
    if yourMin == friendsMin and yourMax == friendsMax:
        return True
    
    else:
        return False
