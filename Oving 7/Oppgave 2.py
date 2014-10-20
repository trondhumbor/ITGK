__author__ = "Tsh"

# a)
import math

def is_prime(zahl):
    for number in range(math.ceil(math.sqrt(zahl))):
        if number % zahl == 0:
            return False
    return True

# b)

def tresher(numbers, treshold):
    less = []
    more = []

    for number in numbers:
        if number < treshold:
            less.append(number)
        else:
            more.append(number)
    return less, more

# c)
def multiplication_table(n):
    toplist = []
    n = n + 1
    for x in range(1,n):
        sublist = []
        for y in range(1,n):
            sublist.append(x*y)
        toplist.append(sublist)
    return toplist



if __name__ == "__main__":
    #print(is_prime(11))
    #print(tresher([0,1,2,3,4,5], 3))

    for li in multiplication_table(3):
        print(li)