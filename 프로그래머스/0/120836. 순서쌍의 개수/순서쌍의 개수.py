def solution(n):
    count = 0
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            count += 1
    
    return count*2 if int(n**(1/2)) != n**(1/2) else count*2-1