n, m = map(int, input().split())
lst = [0]*n
for _ in range(m):
  i, j, k = map(int, input().split())
  for a in range(i-1,j):
    lst[a] = k
print(" ".join(map(str, lst)))