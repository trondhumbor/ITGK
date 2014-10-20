# Oppgave 1

import random

def center_of_mass(liste):

    # Vi vet fra Fysikk 2 på videregående skole, at massesenteret er gitt ved
    # massesentrum = (masse_1 * lengde_1) + (masse_2 * lengde_2) ... (masse_n * lengde_n) / (masse_1 + masse_2 + ... + masse_n)

    # en halvmeter mer enn elementets index i lista vil betegne lengden
    teller = 0
    nevner = 0

    for index in range(len(liste)):
        teller += liste[index] * (0.5 + index)
        nevner += liste[index]

    return teller / nevner

if __name__ == "__main__":
    # a)
    print ( center_of_mass ([1]) ) # 0.5
    print ( center_of_mass ([1 , 1]) ) # 1
    print ( center_of_mass ([1 , 1 , 1]) ) # 1.5
    print ( center_of_mass ([3 , 1 , 3]) )  # 1.5
    print ( center_of_mass ([1 , 2 , 3 , 4]) ) # 2. 6667
    # b)
    liste = []
    for i in range(100):
        liste.append(random.random())
    print ( center_of_mass (liste) )