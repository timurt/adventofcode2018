f = open('input.txt')

arr = []
max_len = 0
while True:
    line = f.readline()
    if not line:
        break

    arr.append(line)
    max_len = max(max_len, len(line))

res = ''
found = False
for i in range(0, max_len - 1):
    my_set = set()
    for line in arr:
        new_line = line[0:i] + line[i+1:]
        if new_line in my_set:
            found = True
            res = new_line
            break
        else:
            my_set.add(new_line)
    if found:
        break

print(res)
f.close()
