# Non-ASCIItegn er en uting
input_kjonn = None
input_alder = 0
aktiv_sosiale_medier = False
medlem_facebook = False

def main():
    input_kjonn = str(input("Hvilket kjonn er du? (m/k) "))
    input_alder = int(input("Hvor gammel er du? (heltall) "))

    if input_alder < 16 or input_alder > 25:
        print("Du er ikke innenfor malgruppen. Avslutter...")
        return

    # Vi vet fra na at brukeren er innenfor tiltenkt aldersgruppe
    aktiv_sosiale_medier = str(input("Benytter du ett eller flere sosiale medier? (ja/nei) "))

    if aktiv_sosiale_medier == "nei":
        print("Du trenger ikke svare pa flere sporsmal. Du kan ga.. for na..")
        return

    if(input_kjonn == "k"):
        medlem_facebook = str(input("Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse? (ja/nei) "))
    elif (input_kjonn == "m"):
        medlem_facebook = str(input("Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse? (ja/nei) "))

    # Det star ikke i oppgaveteksten at vi skal lagre svaret
    input("Hvor mange timer bruker du pa sosiale medier?: ")

    # Jeg tror ikke program-minnet blir clear'a etter at programmet terminerer, men det blir markert som ledig for andre programmer.
    # Om dette stemmer, kan man hente ut det som la i minnet nar programmet terminerte.
    # Hvis minnet faktisk blir clear'a, er variablene og annen programdata lagret i minnet tapt for godt.
    # Evt. kan man skrive variablene til en persistent lagringsplass, da vil det alltid kunne faes tak i pa nytt.

    # Oppgave 2 er den samme som i oving 3.
if __name__ == "__main__":
    main()
