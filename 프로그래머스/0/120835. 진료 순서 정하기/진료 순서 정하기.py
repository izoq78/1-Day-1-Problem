def solution(emergency):
    result = [None]*len(emergency)
    s = 1
    for i in sorted(emergency, reverse=True): # 76 24 3
        n = emergency.index(i)
        result[n] = s
        s += 1
        
    return result