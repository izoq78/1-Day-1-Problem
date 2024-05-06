def solution(n):
    count = 0
    
    while (count<=500):
        if n == 1:
            return count
        
        if n%2==0:
            n /= 2
            count += 1
        else:
            n = n*3+1
            count += 1        
        
    return -1

