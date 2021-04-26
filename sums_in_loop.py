out = []
for x in range(int(input())):
    a, b = input().split()
    sum = int(a) + int(b)
    out.append(sum)
print(*out, sep=' ')
