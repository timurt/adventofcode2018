def calculate(line):
    l = line.lower()
    i = 0
    while (i + 1) < len(line):
        if (line[i] != line[i + 1]) and (l[i] == l[i + 1]):
            line = line[0:i] + line[i + 2:]
            l = l[0:i] + l[i + 2:]
            if i > 0:
                i -= 1
        else:
            i += 1
    return len(line)


def solve():
    f = open('input.txt')
    line = f.readline()
    print calculate(line)
    f.close()


solve()
