import sys

def getVisibleRow(row: int, column: int, value: int, input) -> bool:

    visibleRight = True
    for i in input[row][column+1: ]:
        if (i >= value):
            visibleRight = False
            break

    if (not visibleRight):
        visibleLeft = True
        for i in input[row][ :column]:
            if (i >= value):
                visibleLeft = False
                break
    
    return visibleRight or visibleLeft


def getVisibleColumn(row: int, column: int, value: int, input) -> bool:

    visibleDown = True
    for i in input[row+1: ]:
        if (i[column] >= value):
            visibleDown = False
            break

    if (not visibleDown):
        visibleUp = True
        for i in input[: row]:
            if (i[column] >= value):
                visibleUp = False
                break

    return visibleDown or visibleUp


def getVisible(row: int, column: int, input) -> int:

    value = input[row][column]
    visible = getVisibleRow(row, column, value, input)
    
    if (not visible):
        visible = getVisibleColumn(row, column, value, input)
    
    return visible

if __name__ == "__main__":
    input = open(sys.argv[1]).read().split("\n")

    columnMax = len(input[0]) -1
    rowMax = len(input) -1
    visible = 0

    row = 0
    for line in input: # for every row
        column = 0
        for i in line:# for column row of said row
            if (row == 0 or row == rowMax) or \
            (column == 0 or column == columnMax):
                visible += 1
            else:
                
                visible += getVisible(row, column, input)

            column += 1
        row += 1

    print(f"There are {visible} visible trees.")