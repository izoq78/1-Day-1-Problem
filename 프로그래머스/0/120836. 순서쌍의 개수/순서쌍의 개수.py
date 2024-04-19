def solution(n):
    answer = 0
    n2 = int(n**(1/2))
    
    for i in range(1,n2+1):
        if(n%i==0):
            answer += 1
        
    return answer*2-1 if n2==n**(1/2) else answer*2