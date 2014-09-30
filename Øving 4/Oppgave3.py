# Øving i ITGK
# Trond Humborstad

def billettpris(alder):
    # Python burde skaffe seg et switch-case-statement, slik som
    # andre programmeringsspråk.

    if alder > 60:
        print("Billettpris: Gratis. Prisklasse: Honnoer")
        return
    elif alder > 26:
        print("Billettpris: 40kr. Prisklasse: Voksen")
        return
    elif alder > 21:
        print("Billettpris: 30kr. Prisklasse: Student")
        return
    elif alder > 16:
        print("Billettpris: 20kr. Prisklasse: Ungdom")
        return
    elif alder > 5:
        print("Billettpris: 10. Prisklasse: Barn")
        return
    elif alder > 0:
        print("Billettpris: Gratis. Prisklasse: Smaabarn")
        return

if __name__ == "__main__":
    test = True
    if test:
        billettpris(3)
        billettpris(12)
        billettpris(18)
        billettpris(23)
        billettpris(40)
        billettpris(80)
    else:
        alder = int(input("Hvor gammel er du? (heltall) "))
        billettpris(alder)