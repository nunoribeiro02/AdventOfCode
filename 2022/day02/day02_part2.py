import fileinput

def compareRoud(line):
    #extract play
    opPlay = ord(line[0]) - ord('A')  
    myPlay = line[2]

    # score
    score = 0
    shape = 0
    
    if (myPlay == 'X'): #lose
        shape = (opPlay+2) %3 +1
    elif (myPlay == 'Y'): #draw
        shape = opPlay +1
        score += 3
    elif (myPlay == 'Z'): #win
        shape = (opPlay-2) %3 +1
        score += 6
    
    score += shape
    print("opplay", opPlay, "shape", shape, "score", score)
    return score


if __name__ == "__main__":
    input = fileinput.input()

    totalScore = 0
    for line in input:
        totalScore += compareRoud(line)

    print("The total score if everything goes exactly according to my strategy guide is:"
          , totalScore)