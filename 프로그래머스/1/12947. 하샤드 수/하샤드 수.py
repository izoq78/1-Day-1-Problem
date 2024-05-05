def solution(x):
    summ = sum(map(int,str(x)))
    return True if x%summ==0 else False