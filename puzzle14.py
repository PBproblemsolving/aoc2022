import sys

grid = set()
sand_grid = set()

def rock_move(start, goal):
    x_start, y_start = start
    x_goal, y_goal = goal
    grid.add(start)
    grid.add(goal)
    if x_start != x_goal:
        if x_start > x_goal:
            step = -1
        else:
            step = 1
        for c in range(x_start, x_goal, step):
            grid.add((c, y_start))
    else:
        if y_start > y_goal:
            step = -1
        else:
            step = 1
        for c in range(y_start, y_goal, step):
            grid.add((x_start, c))

def sand_move(left_min, left_max, down_max):
    settled = False
    freefall = False
    position = (500, 0)
    while not settled and not freefall:
        x, y = position
        if x <= left_max and x >= left_min and y <= down_max:
            if (x, y+1) not in (grid | sand_grid):
                position = (x, y+1)
            elif (x-1, y+1) not in (grid | sand_grid):
                position = (x-1, y+1)
            elif (x+1, y+1) not in (grid | sand_grid):
                position = (x+1, y+1)
            else:
                settled = True
        else:
            freefall = True
    return position, freefall
    
def sand_move_part2(floor):
    settled = False
    position = (500, 0)
    while not settled:
        x, y = position
        if y == floor -1:
            settled = True
        else:
            if (x, y+1) not in (grid | sand_grid):
                position = (x, y+1)
            elif (x-1, y+1) not in (grid | sand_grid):
                position = (x-1, y+1)
            elif (x+1, y+1) not in (grid | sand_grid):
                position = (x+1, y+1)
            else:
                settled = True
    return position


name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.rstrip() for line in f]
    for i, path in enumerate(f):
        path = path.split('-> ')
        subpath = [x.split(',') for x in path]
        f[i] = [(int(x), int(y)) for x, y in subpath]

for rock in f:
    for x, path in enumerate(rock):
        try:
            rock_move(path, rock[x+1])
        except IndexError:
            pass

left_min = min([x[0] for x in grid])
left_max = max([x[0] for x in grid])
down_max = max([x[1] for x in grid])
floor = down_max + 2

for f in range(left_min, left_max, 1):
    grid.add((f, floor))

count = 0
while (500, 0) not in sand_grid:
    count += 1
    sand_position = sand_move_part2(floor)
    sand_grid.add(sand_position)
    print(sand_position)



for y in range(down_max+3):
    for x in range(left_max-left_min+1):
        if (x+left_min, y) in grid:
            print('#',end='')
        elif (x+left_min, y) in sand_grid:
            print('o', end='')
        else:
            print('.',end='')
    print('\n')

print(count)