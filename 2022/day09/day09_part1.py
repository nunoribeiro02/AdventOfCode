import sys

class Head:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dir):
        if dir == 'R':
            self.x += 1
        elif dir == 'L':
            self.x -= 1
        elif dir == 'U':
            self.y += 1
        elif dir == 'D':
            self.y -= 1


class Tail(Head):
    def __init__(self):
        super().__init__()
        self.pos = set()

    def follow(self, head):
        if (abs(head.x - self.x) > 1 or abs(head.y - self.y) > 1):
            if (head.x > self.x):
                self.x += 1
            elif (head.x < self.x):
                self.x -= 1

            if (head.y > self.y):
                self.y += 1
            elif (head.y < self.y):
                self.y -= 1

        self.pos.add((self.x, self.y))

if __name__ == "__main__":
    input = open(sys.argv[1]).read().split("\n")

    head = Head()
    tail = Tail()
    for line in input:
        dir = line[0]
        amount = int(line[2:])
        
        while (amount > 0):
            head.move(dir)
            tail.follow(head)

            amount -= 1
    
    print(f"The tail of the rope visits {len(tail.pos)} positions at least once.")