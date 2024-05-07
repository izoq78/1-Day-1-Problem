def solution(price, money, count):
    s = sum(price*i for i in range(1,count+1))
    return 0 if s<=money else s-money