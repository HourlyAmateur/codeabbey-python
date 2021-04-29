out = []
for x in range(int(input())):
    a, b, c = input().split()
    out.append(min(int(c), min(int(a),int(b))))
print(*out)