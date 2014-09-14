import math

def closestToN(n):
    iterativeSum = 0
    currentInteger = 1
    elements = 0

    # math.pow tilsvarer **
    while (iterativeSum + math.pow(currentInteger, 2)) < n:
        iterativeSum += math.pow(currentInteger, 2)
        currentInteger += 1
        elements += 1

    return iterativeSum, elements

if __name__ == "__main__":
    print(closestToN(10))