def solution(arr, queries):
    result = []
    for i in range(len(queries)):
        r = []
        for j in range(queries[i][0], queries[i][1]+1): 
            if arr[j]>queries[i][2]:
                r.append(arr[j])
        if r==[]:
            result.append(-1)
        else:
            result.append(min(r))
            
    return result