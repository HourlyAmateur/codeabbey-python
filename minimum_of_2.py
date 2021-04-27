out = []
for x in range(int(input())):
    a, b = input().split()
    out.append(min(int(a),int(b)))
print(*out)