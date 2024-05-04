def solution(n):
    nn = n**(1/2)
    return (nn+1)**2 if nn==int(n**(1/2)) else -1