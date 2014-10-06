import sys

antall_kvinner = 0
antall_menn = 0
antall_sosmedier = 0
antall_facebook = 0
antall_timer_sosmedier = 0

def validate(userInput):
    if str(userInput) == "hade":
        print("Antall kvinner",antall_kvinner,
              "Antall menn", antall_menn,
              "Antall sosmed", antall_sosmedier,
              "Antall facebook", antall_facebook,
              "Antall timer sosmed", antall_timer_sosmedier)
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
                getInput("Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse? ")
            elif kjonn == "m":
                getInput("Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse? ")

            timer_sosmedier = float(getInput("Hvor mange timer bruker du gjennomsnittlig per dag paa sosiale medier? "))

if __name__ == "__main__":
    main()