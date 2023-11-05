import sys

def normalizePriority(char : str) -> int:
    priority = ord(char)
    minLowerPri = 1
    minUpperPri = 27
    if (char.islower()):
        priority += minLowerPri - ord('a') 
    else: # uppercase letters
        priority += minUpperPri - ord('A') 

    return priority
        

if __name__ == "__main__":
    input = open(sys.argv[1]).read().strip().split()

    totalPriority = 0
    for line1, line2, line3 in zip(input[::3], input[1::3], input[2::3]):

        commonChar = (set(line1) & set(line2) & set(line3)).pop()

        #commonChar = commonChar.pop() if (len(commonChar) == 1) else 'a'
        priority = normalizePriority(commonChar)

        totalPriority += priority

    print("The sum of the priorities of those item types is", totalPriority)