def solution(my_string, s, e):
    st = my_string[s:e+1]
    return my_string[:s] + st[::-1] + my_string[e+1:]