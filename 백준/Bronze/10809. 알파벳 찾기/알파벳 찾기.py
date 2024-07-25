import string

s = input()
for i in string.ascii_lowercase:
  print(s.index(i) if i in s else -1, end=" ")