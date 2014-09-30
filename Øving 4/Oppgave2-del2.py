import sys

antall_kvinner = 0
antall_menn = 0
antall_sosmedier = 0
antall_facebook = 0
antall_timer_sosmedier = 0

def validate(userInput):
    if str(userInput) == "hade":
        print(antall_kvinner, antall_menn, antall_sosmedier, antall_facebook, antall_timer_sosmedier)
        sys.exit()

def getInput(querystring):
    userInput = input(querystring)
    validate(userInput)
    return userInput

def main():
    # Run program forever

    while True:

        kjonn = ""
        alder = 0
        aktiv_sosmedier = ""
        aktiv_facebook = ""
        timer_sosmedier = 0

        while alder > 25 or alder < 16:

            kjonn = str(getInput("Er du mann eller kvinne? (m/k) ")) 
            alder = int(getInput("Hvor gammel er du? (heltall) "))
            
            if alder > 25 or alder < 16:
                print("Du kan ikke ta sporreundersokelsen.")

        aktiv_sosmedier = str(getInput("Er du aktiv på sosiale medier? (ja/nei) "))
        if aktiv_sosmedier == "ja":
            if kjonn == "k":
                # I denne deloppgaven skal ikke svaret lagres til en variabel
                aktiv_facebook = str(getInput("Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse? "))
            elif kjonn == "m":
                aktiv_facebook = str(getInput("Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse? "))

            timer_sosmedier = float(getInput("Hvor mange timer bruker du gjennomsnittlig per dag paa sosiale medier? "))

        global antall_menn
        global antall_kvinner
        global antall_sosmedier
        global antall_facebook
        global antall_timer_sosmedier

        if kjonn == "m":
            antall_menn += 1
        elif kjonn == "k":
            antall_kvinner += 1

        if aktiv_sosmedier == "ja":
            antall_sosmedier += 1
            antall_timer_sosmedier += timer_sosmedier

        if aktiv_facebook == "ja":
            antall_facebook += 1


if __name__ == "__main__":
    main()