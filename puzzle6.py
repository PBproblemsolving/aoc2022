import sys

name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.rstrip() for line in f][0]

print(f)

n = 13
while n<= len(f):
    checked = f[n-13:n+1]
    if len(set(checked)) == len(checked):
        print(n+1)
        print(checked)
        break
    n += 1