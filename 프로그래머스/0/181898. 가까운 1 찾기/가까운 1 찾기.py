def solution(arr, idx):
    arr = arr[idx:]
    return idx + arr.index(1) if 1 in arr else -1