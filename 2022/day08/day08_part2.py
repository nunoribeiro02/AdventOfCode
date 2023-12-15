import sys

def getScenicScoreRows(row: int, column: int, value: int, input) -> bool:
    scoreRight = 0

    for i in input[row][column+1: ]:
        scoreRight += 1
        if (i >= value):
            break
    
    scoreLeft = 0
    for i in reversed(input[row][ :column]):
        scoreLeft += 1
        if (i >= value):
            break
    
    return scoreRight * scoreLeft


def getScenicScoreColumns(row: int, column: int, value: int, input) -> bool:
    scoreDown = 0
    for i in input[row+1: ]:
        scoreDown += 1
        if (i[column] >= value):
            break
    
    scoreUp = 0
    for i in reversed(input[: row]):
        scoreUp += 1
        if (i[column] >= value):
            break

    return scoreUp * scoreDown

def getScenicScore(row: int, column: int, input) -> int:

    value = input[row][column]
    scoreRows = getScenicScoreRows(row, column, value, input)
    scoreColumns = getScenicScoreColumns(row, column, value, input)

    return scoreRows * scoreColumns

if __name__ == "__main__":
    input = open(sys.argv[1]).read().split("\n")

    columnMax = len(input[0]) -1
    rowMax = len(input) -1
    scenicScore = 0

    row = 0
    for line in input: # for every row
        column = 0
        for i in line:# for column row of said row
            score = 0
            if (row == 0 or row == rowMax) or \
            (column == 0 or column == columnMax):
                column += 1
                continue
            else:
                score = getScenicScore(row, column, input)

            scenicScore = max(score, scenicScore)
            column += 1

        row += 1

    print(f"The highest scenic score possible for any tree is {scenicScore}")