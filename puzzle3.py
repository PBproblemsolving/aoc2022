import sys
import string


name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.strip() for line in f]
    items = []
    for line in f:
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        items.append([firstpart, secondpart])

alphabet = list(string.ascii_letters)
values_abc = range(1, 53)
priority = {a:b for a, b in zip(alphabet, values_abc)}

score = 0
for item in items:
    score += int(priority[(list(set(item[0]) & set(item[1])))[0]])

n = 0
support_lines = []
score2 = 0
for line in f:
    support_lines.append(set(line))
    n += 1
    if n == 3:
        print(support_lines)
        badge = list(set(line).intersection(*support_lines))[0]
        score2 += int(priority[badge])
        support_lines = []
        n = 0

print(score2)