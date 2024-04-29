def solution(quiz):
    result = []
    
    for i in quiz:
        i = i.replace(" ",'')
        a,b = i.split('=')
        
        result.append("O" if eval(a) == int(b) else "X")
        
    return result