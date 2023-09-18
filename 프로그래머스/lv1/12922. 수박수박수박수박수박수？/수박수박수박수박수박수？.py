def solution(n):
    str = "수박"
    if n%2==0:
        n = int(n/2)
        str = str*n
    else:
        n = int(n//2)
        str = str*n + "수"
        
    answer = str
    return answer