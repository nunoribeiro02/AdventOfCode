import fileinput

if __name__ == "__main__":
    input = fileinput.input()
    
    
    maxElf = 0
    currentElf = 0

    for line in input:
        if (line != '\n'):
            currentElf += int(line)
        else:
            if (currentElf > maxElf):
                maxElf = currentElf
            
            
    #check for the last line        
    if (currentElf > maxElf):
        maxElf = currentElf    

    print("The Elf carrying the most Calories is: ", maxElf)
