def solution(arr):
    if 2 not in arr:
        return [-1]
    n = arr.index(2)
    m = arr[::-1].index(2)
    
    return arr[n:] if arr[-1] == 2 else arr[n:-m]