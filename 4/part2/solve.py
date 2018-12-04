def get_guard_id(line):
    g_id = int(line[line.index('Guard') + 7: line.index('begins') - 1])
    return g_id


def is_guard(line):
    return line[19:].startswith('Guard')


def get_date(line):
    year = int(line[1:5])
    month = int(line[6:8])
    day = int(line[9:11])
    hours = int(line[12:14])
    minutes = int(line[15:17])
    date = (day * 24) + hours
    date = (date * 60) + minutes
    return date


def parse_line(line):
    x = int(line[line.index('@') + 2: line.index(',')])
    y = int(line[line.index(',') + 1: line.index(':')])
    w = int(line[line.index(':') + 2: line.index('x')])
    h = int(line[line.index('x') + 1:])
    return x, y, w, h


def solve():
    f = open('input.txt')

    arr = []
    day_min = 60
    while True:
        line = f.readline()

        if not line:
            break
        if len(line.strip()) > 0:
            arr.append(line)

    arr.sort()
    my_map = {}
    sum_map = {}
    max_map = {}
    i = 0

    max_guard_id = -1
    while i < len(arr):
        guard_id = get_guard_id(arr[i])

        if guard_id in my_map:
            day_arr = my_map[guard_id]
            guard_sum = sum_map[guard_id]
            guard_max = max_map[guard_id]
        else:
            day_arr = []
            guard_sum = 0
            guard_max = 0
            for j in range(0, day_min + 1):
                day_arr.append(0)
        i += 1
        if not is_guard(arr[i]):
            while True:
                start_date = get_date(arr[i])
                end_date = get_date(arr[i + 1])
                while start_date < end_date:
                    guard_sum += 1
                    day_arr[start_date % day_min] += 1
                    if day_arr[start_date % day_min] > day_arr[guard_max]:
                        guard_max = start_date % day_min
                    start_date += 1
                i += 2

                if i >= len(arr) or is_guard(arr[i]):
                    break
        my_map[guard_id] = day_arr
        sum_map[guard_id] = guard_sum
        max_map[guard_id] = guard_max

        if max_guard_id == -1:
            max_guard_id = guard_id
        else:
            if my_map[guard_id][max_map[guard_id]] > my_map[max_guard_id][max_map[max_guard_id]]:
                max_guard_id = guard_id

    res = max_map[max_guard_id] * max_guard_id
    print res
    f.close()


solve()
