def get_type(line):
    occur = {}
    for c in line:
        if c in occur:
            occur[c] = occur[c] + 1
        else:
            occur[c] = 1
    exact_two = False
    exact_three = False

    for value in occur.values():
        if value == 2:
            exact_two = True
        elif value == 3:
            exact_three = True

    if exact_three & exact_two:
        return 2
    elif exact_two:
        return 0
    elif exact_three:
        return 1
    else:
        return -1


f = open('input.txt')

first_type = 0
second_type = 0

while True:
    line = f.readline()
    if not line:
        break
    id_type = get_type(line)
    if id_type == 0:
        first_type += 1
    elif id_type == 1:
        second_type += 1
    elif id_type == 2:
        first_type += 1
        second_type += 1

res = first_type * second_type
print(res)

f.close()
