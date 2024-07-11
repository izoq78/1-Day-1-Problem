n, x = map(int, input().split())
a = [int(i) for i in input().split() if int(i)<x]
for i in a:
  print(i,end=' ')