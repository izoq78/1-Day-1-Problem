def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        s = ''.join(my_strings[i][parts[i][0]:parts[i][1]+1])
        answer += s
    return answer