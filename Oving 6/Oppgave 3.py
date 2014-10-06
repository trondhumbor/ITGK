__author__ = "Tsh"

# Dette var en veldig merkelig oppgave, med tidvis rar formulering
# Tror jeg har tolket den rett.

vec1 = []

# a
def getInput():
    return [int(element) for element in input("Skriv inn xyz-verdiene på formen: x y z ").split(" ")]

# b
def prettyprint():
    global vec1
    vec1 = getInput()
    print("x: ", vec1[0], " y: ", vec1[1], " z: ", vec1[2])


# c
def vectormultiplication(vec, scal):
    newvec = []
    for element in vec:
        newvec.append(element * scal)
    return newvec

def doVectorMultiplication():
    global vec1
    inputscalar = int(input("Skriv inn en skalar: "))
    vec1 = vectormultiplication(vec1, inputscalar)
    print(vec1)

# d
def vectorlength(vec):
    veclen = ((vec[0]**2) + (vec[1]**2) + (vec[2]**2))**0.5
    print(veclen)

def vectorMultiplicationModified(vec, scal):
    newvec = []
    vectorlength(vec)
    for element in vec:
        newvec.append(element * scal)
    vectorlength(vec)
    return newvec

# e
def indreprodukt(vec1, vec2):
    return (vec1[0]*vec2[0]) + (vec1[1]*vec2[1]) + (vec1[2]*vec2[2])

def lesInnOgMultipliserVec1ogVec2():
    vec2 = getInput()
    print(indreprodukt(vec1, vec2))
