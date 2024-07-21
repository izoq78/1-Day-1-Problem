n = int(input())
lst = [int(i) for i in input().split()]

sum = 0
Max = max(lst)
for i in lst:
  sum += i/Max*100
print(sum/n)