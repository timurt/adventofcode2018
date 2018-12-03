f = open('input.txt')

arr = []
while True:
    line = f.readline()
    if not line:
        break
    arr.append(int(line))

frequencySet = {0}

cur = 0
notFound = True
while notFound:
    for x in arr:
        cur += x
        if cur in frequencySet:
            notFound = False
            break
        frequencySet.add(cur)

print(cur)
f.close()