d = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s = input()
result = 0
for i in s:
  for dd in d:
    if i in dd:
      result += d.index(dd)+3
print(result)