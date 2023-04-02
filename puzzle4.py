import sys

name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.strip() for line in f]

f = [line.split(',') for line in f]
sections = []
for line in f:
    pair_of_elves = []
    for elf in line:
        elf = elf.split('-')
        elf = tuple([int(coord) for coord in elf])
        pair_of_elves.append(elf)
    sections.append(tuple(pair_of_elves))

print(sections)
counter = 0
for pair in sections:
    if pair[0][0] >= pair [1][0] and pair[0][1] <= pair[1][1] or pair[1][0] >= pair [0][0] and pair[1][1] <= pair[0][1]:
        counter += 1

print(counter)

print(sections)
counter2 = 0
for pair in sections:
    if pair[0][1] < pair [1][0] and pair[0][1] < pair[1][0] or pair[1][1] < pair [0][0] and pair[1][1] < pair[0][0]:
        counter2 += 1

print(len(sections) - counter2)