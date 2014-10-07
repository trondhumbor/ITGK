__author__ = "Tsh"

# Greedy algorithm incoming

pricePerGram = 0.5
availableCoins = [20, 10, 5, 1, 0.5]

def getValueFromWeigth(weight):
    return weight * pricePerGram

def greedy(valueToGive):
    coinsToReturn = [0, 0, 0, 0, 0]
    for index, coin in enumerate(availableCoins):
        d = 0 # d counts the coins of denomination c_i used
        while valueToGive >= coin:
            d += 1 # add a coin of denomination c_i
            valueToGive -= coin
        coinsToReturn[index] = d
    return coinsToReturn

def main():
    teeth = [95 , 103 , 71 , 99 , 114 , 64 , 95 , 53 , 97 , 114 ,
             109 , 11 , 2 , 21 , 45 , 2 , 26 , 81 , 54 , 14 ,
             118 , 108 , 117 , 27 , 115 , 43 , 70 , 58 , 107
    ]
    for tooth in teeth:
        value = getValueFromWeigth(tooth)
        coinsToReturn = greedy(value)
        print(value, coinsToReturn)

if __name__ == "__main__":
    main()