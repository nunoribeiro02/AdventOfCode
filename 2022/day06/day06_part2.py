import sys

def allDifferent(signal: str) -> bool:
    different = True
    for i in range(len(signal)):
        for j in range(i+1, len(signal)):
            if (signal[i] == signal[j]):
                different = False
                break
        if not different:
            break
    
    return different

if __name__ == "__main__":
    input = open(sys.argv[1]).read()
    indexUpper = 4
    indexLower = 0
    signal = input[indexLower : indexUpper]

    while (not allDifferent(signal)):
        indexUpper += 1
        indexLower += 1
        signal = input[indexLower : indexUpper]

    print(f"{indexUpper} characters need processed before the first start-of-message marker is detected")