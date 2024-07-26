n = int(input())
for _ in range(n):
  i, s = map(str, input().split())
  for j in range(len(s)):
    print(int(i)*s[j], end="")
    if j==len(s)-1:
      print()