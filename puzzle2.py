import sys

name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.strip().split() for line in f]



def calculate(round:list) -> int:
    opponent, you  = round
    cheap_score = {'X': 1, 'Y': 2, 'Z': 3}
    score = cheap_score[you]
    if opponent == 'A':
        if you == 'X':
            score += 3
        elif you == 'Y':
            score += 6
        elif you == 'Z':
            score += 0
    elif opponent == 'B':
        if you == 'X':
            score += 0
        elif you == 'Y':
            score += 3
        elif you == 'Z':
            score += 6
    elif opponent == 'C':
        if you == 'X':
            score += 6
        elif you == 'Y':
            score += 0
        elif you == 'Z':
            score += 3
    return score
score = 0
for line in f:
    score += calculate(line)

print(score)

score = 0

outcomes = {'A': {'X': 'C', 'Y': 'A', 'Z': 'B'},
            'B': {'X': 'A', 'Y': 'B', 'Z': 'C'},
            'C': {'X': 'B', 'Y': 'C', 'Z': 'A'}}

def calculate_second(round: list) -> int:
    opponent, result  = round
    big_score = {'X': 0, 'Y': 3, 'Z': 6}
    cheap_score = {'A': 1, 'B': 2, 'C': 3}
    score = big_score[result]
    you = outcomes[opponent]
    you = you[result]
    score += cheap_score[you]
    return score

for line in f:
    print(calculate_second(line))
    score += calculate_second(line)

print(score)
