def solution(ineq, eq, n, m):

    return int(eval(str(n)+ineq+eq+str(m))) if eq=='=' else int(eval(str(n)+ineq+str(m)))