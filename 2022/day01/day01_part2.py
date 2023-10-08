import fileinput

def compareElfs(currentElf, topElfs):
    if (currentElf >= topElfs[0]):
        topElfs[2] = topElfs[1]
        topElfs[1] = topElfs[0]
        topElfs[0] = currentElf
    elif (currentElf >= topElfs[1]):
        topElfs[2] = topElfs[1]
        topElfs[1] = currentElf
    elif (currentElf > topElfs[2]):
        topElfs[2] = currentElf

if __name__ == "__main__":
    input = fileinput.input()
    
    currentElf = 0
    topElfs = [0, 0, 0]

    for line in input:
        if (line != '\n'):
            currentElf += int(line)
        else:
            compareElfs(currentElf, topElfs)
            currentElf = 0
        
    #check for the last line        
    compareElfs(currentElf, topElfs)

    sumTopElfs = topElfs[0] + topElfs[1] + topElfs[2]

    print("The top 3 Elfs carrying the most Calories are:",
           topElfs[0], ",", topElfs[1], ",", topElfs[2], "and their sum is:", sumTopElfs)
