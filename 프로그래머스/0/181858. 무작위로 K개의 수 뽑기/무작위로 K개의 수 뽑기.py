def solution(arr, k):
    s = list(dict.fromkeys(arr))
    result = []
    
    for i in range(min(k,len(s))):
        result.append(s[i])
    
    if len(result) != k:
        result.extend([-1]*(k-len(s)))
    
    return result