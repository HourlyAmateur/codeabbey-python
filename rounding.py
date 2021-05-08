out = []
for x in range(int(input())):
    a, b = input().split()
    c = int(a) / int(b)
    if c > 0:
        out.append(int(c + 0.5))
    else:
        out.append(int(c - 0.5))
print(*out, sep=' ')