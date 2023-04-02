import sys
from collections import defaultdict

name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]
coords = {1:1, 5:2, 9:3, 13:4, 17:5, 21:6, 25:7, 29:8, 33: 9}

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.rstrip() for line in f]
    creates = defaultdict(list)
    for line in f:
        if line == '':
            break
        for n, create in enumerate(line):
            if create == '1':
                break
            if n in coords:
                if create != ' ':
                    creates[coords[n]].append(create)

orders = f[f.index('')+1:]
orders = [order.split() for order in orders]
orders = [(int(order[1]), int(order[3]), int(order[5])) for order in orders]
# print(orders)
print(creates)

# for order in orders:
#     for _ in range(int(order[0])):
#         print(creates[order[1]])
#         to_move = creates[order[1]].pop(0)
#         print(to_move)
#         creates[order[2]].insert(0, to_move)
#         print(creates[order[2]])

# tops = ''
# creates = sorted(creates.items())
# print(creates)
# for stack in creates:
#     tops += stack[1][0]

# print(tops)

for order in orders:
    print(creates[order[1]])
    to_move = creates[order[1]][0:order[0]]
    del(creates[order[1]][0:order[0]])
    print(to_move)
    creates[order[2]] = to_move + creates[order[2]]
    print(creates[order[2]])


tops = ''
creates = sorted(creates.items())
print(creates)
for stack in creates:
    tops += stack[1][0]

print(tops)