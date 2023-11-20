import sys

def isOverlap(left: str, right: str) -> bool:

    return ((left[0] <= right[0] and left[1] >= right[0]) or 
        (left[0] <= right[1] and left[1] >= right[1]) or
        (left[0] >= right[0] and left[0] <= right[1]) or 
        (left[1] >= right[0] and left[1] <= right[1]))  


if __name__ == "__main__":
    input = open(sys.argv[1]).read().replace('-', ',').strip().split()
    
    overlaps = 0
    for line in input:
        line = line.split(',') 
        line = [int(i) for i in line]
        m = len(line) //2
        left, right = line[:m], line[m:]

        if (isOverlap(left, right)):
            overlaps += 1

    print("There are", overlaps, "assignment pairs where the ranges overlap")