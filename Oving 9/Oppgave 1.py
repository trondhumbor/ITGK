__author__ = "Tsh"

def getValue_a():
    startsum = 1000
    rente = 0.05
    år = 20
    terminerprår = år / 12

    return startsum * (1 + (rente/terminerprår))**(år*terminerprår)

def getValue_b(startsum, rente, år):
    terminerprår = år / 12

    return startsum * (1 + (rente/terminerprår))**(år*terminerprår)

def getTotalSaved(startsum, rente, år):
    terminerprår = år / 12
    savings = []

    # du får først rente etter ett år
    for year in range(1, år):
        savings.append(startsum * (1 + (rente/terminerprår))**(year*terminerprår))

    return savings

def takeUserInputAndCompute():
    # uklar oppgave, antar man skal skrive ut tabell man får ved
    # å kalle getTotalSaved med brukerinput
    a = float(input("Skriv inn a: "))
    r = float(input("Skriv inn r: "))
    k = int(input("Skriv inn k: "))

    result = getTotalSaved(a, r, k)

    print("År: ", "Oppspart: ")
    for index, value in enumerate(result):
        print(index + 1, "{:0.2f}".format(value))

def getStartValue():
    startsum = 0
    sluttsum = 100000

    rente = 0.05
    år = 20

    while getValue_b(startsum, rente, år) <= sluttsum:
        startsum += 1000 # oppgavetekst sier hele tusenlapper
    return startsum


if __name__ == "__main__":
    print(getStartValue())