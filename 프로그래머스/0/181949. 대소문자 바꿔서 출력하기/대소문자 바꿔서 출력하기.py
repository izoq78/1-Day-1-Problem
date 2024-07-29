str = input()
for s in str:
    print(s.upper() if s.islower() else s.lower(), end="")