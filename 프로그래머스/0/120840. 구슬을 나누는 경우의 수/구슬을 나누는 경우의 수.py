def solution(b, s):
    return (fac(b)) / (fac(b-s)*fac(s))
    
    
def fac(n):
    return n*fac(n-1) if n>1 else 1