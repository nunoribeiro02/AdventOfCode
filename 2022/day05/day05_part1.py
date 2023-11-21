import sys

def getCrates(stacks: str):
    # Get rid of []
    clean_stack = []
    for level in stacks[:-1]:
        clean_level = []
        for elem in level.split():
            clean_level.append(elem[1])
        
        clean_stack.append(clean_level)
    
    # the same as: stacks = [[print(elem[1]) for elem in level.split()] for level in stacks]

    # Get number of stacks
    crates = [ [] for _ in range(len(clean_stack[0]))]
    for level in reversed(clean_stack):
        for index, value in enumerate(level):
            if value != '!':
                crates[index].append(value)

    return crates


def moveStack(crates: str, line: str):
    nCrates, srcStack, dstStack = int(line[1]), int(line[3]) -1, int(line[5]) -1
    
    while (nCrates > 0):
        value = crates[srcStack].pop()
        crates[dstStack].append(value)
        nCrates -= 1
        
    return crates



if __name__ == "__main__":
    input = open(sys.argv[1]).read()
    
    stacks, moves = input.split("\n\n")
    
    # Mark empty spaces with [!] and remove spaces
    stacks = stacks.replace("    ", " [!] ").split("\n")
    crates = getCrates(stacks)

    moves = moves.split("\n")
    for line in moves:
        crates = moveStack(crates, line.split())

    topStack = ""
    for i in range(len(crates)):
        topStack += crates[i].pop()

    print("The crates at the top of each stack are", topStack)