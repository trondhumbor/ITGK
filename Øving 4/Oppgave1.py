input_kjønn = None
input_alder = 0
aktiv_sosiale_medier = False
medlem_facebook = False

def main():
    input_kjønn = str(input("Hvilket kjønn er du? (m/k): "))
    input_alder = int(input("Hvor gammel er du? (heltall): "))

    if input_alder < 16 and input_alder > 25:
        print("Du er ikke innenfor målgruppen. Avslutter...")
        return
    # Vi vet fra nå at brukeren er innenfor tiltenkt aldersgruppe
    aktiv_sosiale_medier = str(input("Benytter du ett eller flere sosiale medier? (ja/nei)"))

    if aktiv_sosiale_medier == "nei":
        print("Du trenger ikke svare på flere spørsmål. Du kan gå.. for nå..")
        return

    if(input_kjønn == "k"):
        medlem_facebook = str(input("Mellom 55-60%% av Facebook sine brukere er kvinner. Er du en av disse? (ja/nei)"))
    else if (input_kjønn == "m"):
        medlem_facebook = str(input("Mellom 40-45%% av Facebook sine brukere er menn. Er du en av disse? (ja/nei)"))

    # Det står ikke i oppgaveteksten at vi skal lagre svaret
    input("Hvor mange timer bruker du på sosiale medier?")

    # Jeg tror ikke program-minnet blir clear-a etter at programmet terminerer, men det blir markert som ledig for andre programmer.
    # Om dette stemmer, kan man hente ut det som lå i minnet når programmet terminerte.
    # Evt. kan man skrive variablene til en persistent lagringsplass, da vil det alltid kunne fåes tak i på nytt.

    # Oppgave 2 er den samme som i øving 3.