def solution(rank, attendance):
    dic = dict(zip(rank,attendance))
    lst = sorted(dic.items())
    n1,n2,n3 = [i[0] for i in lst if i[1] == True][:3]
    dic = list(dic)
    
    a = dic.index(n1)
    b = dic.index(n2)
    c = dic.index(n3)
    
    return 10000*a + 100*b + c