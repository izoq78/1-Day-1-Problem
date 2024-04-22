def solution(my_string):
    s = ''.join(s if s.isdigit() else ' ' for s in my_string)
    return sum(int(i) for i in s.split())