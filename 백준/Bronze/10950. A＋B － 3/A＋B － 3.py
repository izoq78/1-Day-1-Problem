T = int(input())
a = []
for i in range(T):
  A, B = map(int, input().split())
  a.append(A+B)
for i in range(T):
  print(a[i])