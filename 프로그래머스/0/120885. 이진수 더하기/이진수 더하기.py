def solution(bin1, bin2):
    a = int(bin1,2)
    b = int(bin2,2)
    result = bin(a+b)
    
    return result[2:]