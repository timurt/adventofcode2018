def create_2d(n, m):
    twod_list = []
    for i in range(0, n):
        new = []
        for j in range(0, m):
            new.append(0)
        twod_list.append(new)
    return twod_list


def parse_line(line):
    index = line[1: line.index('@') - 1]
    x = int(line[line.index('@') + 2: line.index(',')])
    y = int(line[line.index(',') + 1: line.index(':')])
    w = int(line[line.index(':') + 2: line.index('x')])
    h = int(line[line.index('x') + 1:])
    return index, x, y, w, h


def solve():
    f = open('input.txt')

    arr = create_2d(1000, 1000)
    arr_index = []
    arr_x = []
    arr_y = []
    arr_w = []
    arr_h = []
    while True:
        line = f.readline()

        if not line:
            break
        (index, x, y, w, h) = parse_line(line)
        overlaps = False

        for i in range(0, w):
            for j in range(0, h):
                arr[x + i][y + j] += 1
                if arr[x + i][y + j] > 1:
                    overlaps = True
        if not overlaps:
            arr_index.append(index)
            arr_x.append(x)
            arr_y.append(y)
            arr_w.append(w)
            arr_h.append(h)

    ans = ''
    for k in range(0, len(arr_index)):
        overlaps = False
        index = arr_index[k]
        x = arr_x[k]
        y = arr_y[k]
        w = arr_w[k]
        h = arr_h[k]
        for i in range(0, w):
            for j in range(0, h):
                if arr[x + i][y + j] > 1:
                    overlaps = True
                    break
        if not overlaps:
            ans = index
    print(ans)
    f.close()


solve()