import sys

name = sys.argv
day_number = name[0].split('puzzle')[1].split('.')[0]

with open('input{}.txt'.format(day_number)) as f:
    f = f.readlines()
    f = [line.rstrip() for line in f]
    f = [line.split() for line in f]

class Knot():

    def __init__(self, x, y, predecessor) -> None:
        self.visited = set()
        self.x = x
        self.y = y
        self.predecessor = predecessor
        self.visited.add((self.x, self.y))

    @property
    def coords(self):
        return (self.x, self.y)


start = (0, 0)
knots = []
predecessor = Knot(*start, None)
knots.append(predecessor)
for u in range(10):
    next_knot = Knot(*start, predecessor)
    knots.append(next_knot)
    predecessor = next_knot


def moveFirstPart(head_xy, tail):
    x, y = head_xy
    tail_x, tail_y = tail
    if x > tail_x and y > tail_y:
        tail_y += 1
        tail_x += 1
        return (tail_x, tail_y)
    elif x < tail_x and y < tail_y:
        tail_y -= 1
        tail_x -= 1
        return (tail_x, tail_y)
    elif x < tail_x and y > tail_y:
        tail_x -= 1
        tail_y += 1             
        return (tail_x, tail_y)
    elif x > tail_x and y < tail_y:
        tail_x += 1
        tail_y -= 1            
        return (tail_x, tail_y)
    elif x > tail_x and y == tail_y:
        tail_x += 1            
        return (tail_x, tail_y)
    elif x < tail_x and y == tail_y:
        tail_x -= 1            
        return (tail_x, tail_y)
    elif x == tail_x and y > tail_y:
        tail_y += 1            
        return (tail_x, tail_y)
    elif x == tail_x and y < tail_y:
        tail_y -= 1            
        return (tail_x, tail_y)

def moveHead(direction, head_xy):
    x, y = head_xy
    if direction == 'R':
        x += 1
        return (x, y)
    elif direction == 'L':
        x -= 1
        return (x, y)
    elif direction == 'U':
        y += 1
        return (x, y)
    elif direction == 'D':
        y -= 1
        return (x, y)


def is_touching(head_xy, tail_xy):
    head_x, head_y = head_xy
    tail_x, tail_y = tail_xy
    return abs(head_x + 10000 - (tail_x + 10000)) <= 1 and \
        abs(head_y + 10000 - (tail_y + 10000)) <= 1


for instruction in f:
    direction, step = instruction
    for _ in range(int(step)):
        for knot in knots:
            if not knot.predecessor:
                x, y = moveHead(direction, knot.coords)
                knot.x = x
                knot.y = y
            else:
                if not is_touching(knot.predecessor.coords, knot.coords):
                    x, y = moveFirstPart(knot.predecessor.coords, knot.coords)
                    knot.x = x
                    knot.y = y
                    knot.visited.add(knot.coords)

print(len(knots[9].visited))
