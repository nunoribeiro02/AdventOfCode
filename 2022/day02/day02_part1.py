import fileinput

def compareRoud(line):
    #extract play
    opPlay = ord(line[0]) - ord('A')  
    myPlay = ord(line[2]) - ord('X')

    # score (shape I play + outcome)
    score = myPlay +1
    
    
    if (myPlay == opPlay): #draw
        score += 3
    elif ((myPlay+1) %3 == opPlay):
        # op plays rock vs my scissor
        pass
    elif (myPlay > opPlay or myPlay == (opPlay+1) %3 ): # win
        score += 6
    
    return score


if __name__ == "__main__":
    input = fileinput.input()

    totalScore = 0
    for line in input:
        totalScore += compareRoud(line)

    print("The total score of my strategy is:", totalScore)