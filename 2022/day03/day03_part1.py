import fileinput

def findCommonChar(left : str, right: str) -> str:
    commonChar = ''
    for i in left:
        for j in right:
            if (i == j):
                commonChar = i
                break

    return commonChar

def normalizePriority(char : str) -> int:
    priority = ord(char)
    minLowerPri = 1
    minUpperPri = 27
    if ( ord('a') <= priority and priority <= ord('z')): # lowercase letters
        priority += minLowerPri - ord('a') 
    else: # uppercase letters
        priority += minUpperPri - ord('A') 

    return priority
        

if __name__ == "__main__":
    input = fileinput.input()
    
    totalPriority = 0
    for line in input:
        length = len(line)
        #remove '\n'
        if (line[length-1] == '\n'):
            line = line[: length-1]
            length = len(line)

        middle = length//2

        left = line[ :middle]
        right = line[middle:]

        commonChar = findCommonChar(left, right)
        priority = normalizePriority(commonChar)

        totalPriority += priority

    print("The sum of the priorities of those item types is", totalPriority)