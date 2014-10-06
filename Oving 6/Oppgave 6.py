__author__ = "Tsh"

import random

questions = [
    "Hvordan går det med deg, ",
    "Hvordan liker du å hete ",
    "Hvordan liker du å programmere, "
    # , "How about a nice game of chess?"
    # , "Do you want to play Global Thermonuclear War?"
]

followupQuestions = [
    "Hvorfor synes du ",
    "Hva mener du med ",
    "Kan du si noe mer om "
    # , "Are you sure you don't rather want to play a nice game of chess?"
]

smalltalk = [
    "Fint du synes det ",
    "Så bra ",
    "Helt enig "
    # , "Long time since you've logged on, Professor Falken"
]

def doYouWantToPlayAGame():
    username = str(input("Hva heter du? "))
    answer = ""
    while answer != "hade":
        answer = str(input(random.choice(questions) + username + "? "))
        answer = str(input(random.choice(followupQuestions) + answer + ", " + username + "? "))
        print(random.choice(smalltalk))

if __name__ == "__main__":
    doYouWantToPlayAGame()