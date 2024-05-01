def solution(n):
    i = 2
    result = []
    while(n>1):
        if n%i==0:
            result.append(i)
            n /= i
        else:
            i += 1
    #result = 
    return sorted(list(set(result)))