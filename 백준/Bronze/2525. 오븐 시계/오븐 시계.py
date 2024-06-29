h, m = map(int, input().split())
r = int(input())

h += r//60
m += r%60

if m>=60:
  m -= 60
  h +=1
if h>=24:
  h -= 24
print(h, m)