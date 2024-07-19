n, m = map(int, input().split())
lst = [i for i in range(1,n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  lst[a-1:b] = reversed(lst[a-1:b])
print(" ".join(map(str, lst)))