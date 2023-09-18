def solution(numbers):
    i = [i for i in range(0,10)]
    
    for num in numbers:
        i.remove(num) 
    
    answer = sum(i)
    
    return answer