# Oving 2 ITGK
# Trond Humborstad

# Oppgave 3b
# Utsalgspris på Ford Mondeo 1.8 vil bli 369594.0 kr
# Utsalgspris på Ford Mondeo 1.0 vil bli 341893.5 kr
# Utsalgspris på BMW M5 3.0 vil bli 1033682.0 kr
# Utsalgspris på BMW M5 1.3 vil bli 793989.0 kr


def main():
	print("Et program for å beregne nettopris på bil")

	# Spørr brukeren om bilinfo, typecast desimalverdier til float

	bilNavn = input("Navnet på bilen: ")
	bilBruttopris = float( input("Bruttopris på bilen [kr]: ") )
	bilVekt = float( input("Vekt på bilen [kg]: ") )
	bilHestekrefter = float( input("Antall hestekrefter på bilen [hk]: ") )
	bilUtslipp = float( input("Antall gram Co2-utslipp på bilen [gram]: ") )
	bilMotorvolum = float( input("Motorvolum paa bilen [liter]: ") )

	# Kall beregnpris med variabler som holder input fra bruker
	beregn_pris( bilNavn, bilBruttopris, bilVekt, bilHestekrefter, bilUtslipp, bilMotorvolum )

def beregn_pris(bilNavn, bilBruttopris, bilVekt, bilHestekrefter, bilUtslipp, bilMotorvolum):
	'''	Kalkulerer nettopris til en bil '''
	vektCalculated = bilBruttopris * bilVekt * 0.00034
	hestekrefterCalculated = bilBruttopris * bilHestekrefter * 0.00015
	utslippCalculated = bilBruttopris * bilUtslipp * 0.004
	volumCalculated = bilBruttopris * bilMotorvolum * 0.00055

	nettopris = bilBruttopris + vektCalculated + hestekrefterCalculated + utslippCalculated + volumCalculated
	print("Utsalgspris på",  bilNavn, "vil bli", nettopris, "kr")

if __name__ == "__main__":
	main()