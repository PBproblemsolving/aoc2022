with open('input1.txt') as f:
    f = f.readlines()

callories = []
elf = 0
for line in f:
    if line == '\n':
        callories.append(elf)
        elf = 0
        continue
    elf += int(line.strip())

print(sum(sorted(callories, reverse=True)[0:3]))