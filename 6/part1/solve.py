def parse(line):
    xx = int(line[0: line.index(',')])
    yy = int(line[line.index(',') + 2:])
    return xx, yy


def on_bounds(xx, yy, x_max, y_max):
    res = False
    res |= (xx == 0)
    res |= (yy == 0)
    res |= (xx == x_max)
    res |= (yy == y_max)


def solve():
    f = open('input.txt')

    x_min = 10000
    y_min = 10000
    x_max = -10000
    y_max = -10000

    x = []
    y = []
    z = []
    i = 0
    while True:
        line = f.readline()

        if not line:
            break

        (xx, yy) = parse(line)
        x.append(xx)
        y.append(yy)
        z.append(0)
        x_min = min(x_min, x[i])
        x_max = max(x_max, x[i])
        y_min = min(y_min, y[i])
        y_max = max(y_max, y[i])
        i += 1
    f.close()

    x[:] = [v - x_min for v in x]
    y[:] = [v - y_min for v in y]
    x_max -= x_min
    y_max -= y_min

    ans_index = -1
    for i in range(0, x_max + 1):
        for j in range(0, y_max + 1):
            dist = 10000
            index = 0
            same_dist = 0
            for k in range(0, len(x)):
                cur = abs(x[k] - i) + abs(y[k] - j)
                if dist > cur:
                    dist = cur
                    index = k
                    same_dist = 0
                elif dist == cur:
                    same_dist += 1

            if not on_bounds(x[index], y[index], x_max, y_max) and same_dist == 0:
                z[index] += 1
                if ans_index == -1 or z[index] > z[ans_index]:
                    ans_index = index

    print(z[ans_index])


solve()
