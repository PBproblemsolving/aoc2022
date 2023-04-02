import sys
from collections import defaultdict
import string
import math
import heapq

def check_adjacency(checked, neighbour):
    if power_dict[checked] > power_dict[neighbour]:
        return True
    else:
        return abs(power_dict[checked] - power_dict[neighbour]) <= 1

def relax(u, v, distances):
    if distances[v] > distances[u] + 1:
        distances[v] = distances[u] + 1

name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]
adjacency = defaultdict(list)
power = string.ascii_lowercase
power_dict = {letter: value for letter, value in zip(power, [z for z in range(len(power))])}
power_dict['S'] = power_dict['a']
power_dict['E'] = power_dict['z']
vertices = {}
steps = {}
print(power_dict)

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.rstrip() for line in f]
    for i in range(len(f)):
        for j in range(len(f[0])):
            current = (i, j)
            if f[i][j] == 'S':
                start = current
            elif f[i][j] == 'E':
                end = current
            steps[current] = math.inf
            vertices[current] = f[i][j]
            try:
                if check_adjacency(f[i][j], f[i+1][j]):
                    adjacency[current].append((i+1, j))
            except IndexError:
                pass
            try:
                if check_adjacency(f[i][j], f[i][j+1]):               
                    adjacency[current].append((i, j+1))
            except IndexError:
                pass
            if i - 1 > -1:
                if check_adjacency(f[i][j], f[i-1][j]):
                    adjacency[current].append((i-1, j))
            if j-1 > -1:
                if check_adjacency(f[i][j], f[i][j-1]):
                    adjacency[current].append((i, j-1))




possible_starts = [d for d in vertices if vertices[d] == 'a']

shortest = math.inf
for one in possible_starts:
    for vert in vertices:
        steps[vert] = math.inf
    steps[one] = 0
    to_visit = []
    heapq.heapify(to_visit)
    heapq.heappush(to_visit, (steps[one], one))
    visited = set()
    while to_visit:
        current  = heapq.heappop(to_visit)
        if current[1] in visited: 
            continue
        visited.add(current[1])
        children = adjacency[current[1]]
        for child in children:
            relax(current[1], child, steps)
            heapq.heappush(to_visit, (steps[child], child))

    if steps[end] < shortest:
        shortest = steps[end]

print(shortest)

print(sorted(set([vertices[vert] for vert in visited])))