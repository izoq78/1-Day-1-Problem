def solution(a, b):
    if a>b:
        a,b = b,a
    result = [i for i in range(a,b+1)]
    return sum(map(int, result))