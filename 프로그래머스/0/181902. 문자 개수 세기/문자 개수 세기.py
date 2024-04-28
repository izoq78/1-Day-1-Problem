import string

def solution(my_string):
    lst = [s for s in string.ascii_uppercase] + [s for s in string.ascii_lowercase]
    result = [0 for i in range(len(lst))]
    
    for s in my_string:
        result[lst.index(s)] += 1
        
    return result