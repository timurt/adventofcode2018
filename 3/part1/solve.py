def create_2d(n, m):
    twod_list = []
    for i in range(0, n):
        new = []
        for j in range(0, m):
            new.append(0)
        twod_list.append(new)
    return twod_list


def parse_line(line):
    x = int(line[line.index('@') + 2: line.index(',')])
    y = int(line[line.index(',') + 1: line.index(':')])
    w = int(line[line.index(':') + 2: line.index('x')])
    h = int(line[line.index('x') + 1:])
    return x, y, w, h


def solve():
    f = open('input.txt')

    ans = 0
    arr = create_2d(1000, 1000)
    while True:
        line = f.readline()

        if not line:
            break
        (x, y, w, h) = parse_line(line)
        for i in range(0, w):
            for j in range(0, h):
                arr[x + i][y + j] += 1
                if arr[x + i][y + j] == 2:
                    ans += 1

    print(ans)
    f.close()


solve()