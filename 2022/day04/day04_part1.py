import sys

def isIncluded(left: str, right: str) -> bool:
    return ((left[0] >= right[0] and left[1] <= right[1]) or 
        (left[0] <= right[0] and left[1] >= right[1])) 

if __name__ == "__main__":
    input = open(sys.argv[1]).read().replace('-', ',').strip().split()
    
    contained = 0
    for line in input:
        line = line.split(',') 
        line = [int(i) for i in line]
        m = len(line) //2
        left, right = line[:m], line[m:]

        if (isIncluded(left, right)):
            contained += 1

    print("There are", contained, "assignment pairs where one range fully contain the other")