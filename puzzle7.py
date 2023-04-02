import sys
from collections import defaultdict
import random

random.seed()



name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.rstrip() for line in f]

dir_sizes = defaultdict(int)
dirs_dependencies = defaultdict(list)
sizes = defaultdict(int)

for line in f:
    line = line.split()
    if line[0] == '$':
        if line[-1] == '/':
            current = '/'
            pass
        elif line[-1] == 'ls':
            mode = 'appending'
            pass
        elif line[-1] == '..':
            current = preciding
        else:
            preciding = current
            current = line[-1]
            ls = [file.split('_') for file in dirs_dependencies[preciding]]
            for file in ls:
                if file[0] == current:
                    current = file[0] + '_' + file[1]

    else:
        if line[0] == 'dir':
            dir_name = line[1]
            differential = '_' + str(random.randint(0, 1000000000))
            dir_name += differential
            dirs_dependencies[current].append(dir_name)
        else:
            file_name = line[1] 
            differential = '_' + str(random.randint(0, 1000000000))
            file_name += differential
            dirs_dependencies[current].append(file_name)
            sizes[file_name] = int(line[0])

print(dirs_dependencies)

# while dirs_dependencies.values():
#     pass

def traversal(dir_name, parent=None):
    global dir_sizes
    dir_name = dir_name.split('_')[0]
    for element in dirs_dependencies[dir_name]:
        size = sizes.get(element)
        if size:
            dir_sizes[dir_name] += size
        else:
            traversal(element, dir_name)
    if parent:
        dir_sizes[parent] += dir_sizes[dir_name]

traversal('/')
print(dir_sizes)

sum_sub100000 = sum([size for size in dir_sizes.values() if size < 100000])
print(sum_sub100000)