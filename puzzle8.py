import sys
from collections import defaultdict
import math

name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.rstrip() for line in f]


invisibility = {'y_up': defaultdict(list), 'x_left': defaultdict(list)}

visibility_counter = 0

for y, row in enumerate(f):
    for x, tree in enumerate(row):
        if x == 0 or y == 0 or x == len(row) - 1 or y == len(f) - 1:
            visibility_counter += 1
            continue
        for y_down in range(y+1, len(f)):
            if tree <= f[y_down][x]:
                break
        else:
            visibility_counter += 1 
            continue
        for x_right in range(x+1, len(row)):
            if tree <= f[y][x_right]:
                break
        else:
            visibility_counter += 1
            continue
        #left
        try:
            if tree > sorted(list(row[0:x]), reverse=True)[0]:
                visibility_counter += 1
                continue
        except IndexError:
            visibility_counter += 1
        for y_up in range(y-1, -1, -1):
            if tree <= f[y_up][x]:
                break
        else:    
            visibility_counter += 1
            continue


print(visibility_counter)

scenic_score = 0

for y, row in enumerate(f):
    for x, tree in enumerate(row):
        scenic_tree = []
        if x == 0 or y == 0 or x == len(row) - 1 or y == len(f) - 1:
            continue
        count = 0
        for y_down in range(y+1, len(f)):
            count += 1
            if tree <= f[y_down][x]:
                scenic_tree.append(count)
                break
        else:
            scenic_tree.append(count) 
        count = 0
        for x_right in range(x+1, len(row)):
            count += 1            
            if tree <= f[y][x_right]:
                scenic_tree.append(count)
                break
        else:
            scenic_tree.append(count)
        count = 0
        for x_left in range(x-1, -1, -1):
            count += 1 
            if tree <= row[x_left]:
                scenic_tree.append(count)
                break
        else:
            scenic_tree.append(count)
            visibility_counter += 1
        count = 0 
        for y_up in range(y-1, -1, -1):
            count += 1 
            if tree <= f[y_up][x]:
                scenic_tree.append(count)
                break
        else:    
            scenic_tree.append(count)
        if math.prod(scenic_tree) > scenic_score:
            scenic_score = math.prod(scenic_tree)

print(visibility_counter)
print(scenic_score)