import sys

name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.rstrip() for line in f]
    print(f)

e40 = 0
x = 1
cycle = 1
signal = 0
for instruction in f:
    if cycle == 20 + e40 * 40:
        signal += cycle * x
        e40 += 1
    instruction = instruction.split()
    if instruction[0] == 'noop':
        if cycle == x or cycle + 1 == x or cycle - 1 == x:
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        if cycle % 40 == 0:
            cycle = 0
            print('\n') 
    if instruction[0] == 'addx':
        if cycle == x or cycle + 1 == x or cycle - 1 == x:
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        if cycle % 40 == 0:
            cycle = 0
            print('\n') 
        if cycle == 20 + e40 * 40:
            signal += cycle * x
            e40 += 1
        if cycle == x or cycle + 1 == x or cycle - 1 == x:
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        if cycle % 40 == 0:
            print('\n') 
            cycle = 0
        x += int(instruction[1])

print(signal)
print(cycle)

x = 1
cycle = 0

for instruction in f:
    instruction = instruction.split()
    if instruction[0] == 'noop':
        if cycle == x or cycle + 1 == x or cycle - 1 == x:
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        if cycle % 40 == 0:
            cycle = 0
            print('\n') 
    if instruction[0] == 'addx':
        if cycle == x or cycle + 1 == x or cycle - 1 == x:
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        if cycle % 40 == 0:
            cycle = 0
            print('\n') 
        if cycle == x or cycle + 1 == x or cycle - 1 == x:
            print('#', end='')
        else:
            print('.', end='')
        cycle += 1
        if cycle % 40 == 0:
            cycle = 0
            print('\n') 
        x += int(instruction[1])