a = int(input())
b = int(input())
b0 = b//100
b1 = (b//10)%10
b2 = b%10

i3 = a*b2
i4 = a*b1
i5 = a*b0
i6 = i3+i4*10+i5*100
print(i3)
print(i4)
print(i5)
print(i6)