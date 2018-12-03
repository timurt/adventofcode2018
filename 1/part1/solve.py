f = open('input.txt')

ans = 0
while True:
    line = f.readline()
    if not line:
        break
    ans += int(line)

print(ans)
f.close()