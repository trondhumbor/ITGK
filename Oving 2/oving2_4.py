# Oving 2
# Trond Humborstad

# fahrenheit = (celsius * 9/5) + 32
# celsius = (fahrenheit - 32) / ( 9 / 5 )

def fahrenheitToCelsius():
	fahrenheit = float( input("Skriv inn fahrenheit: ") )
	celsius = ( fahrenheit - 32 ) / (9 / 5)
	# Vanligvis ville jeg restriktert antall desimaler, men oppgaven spørr ikke om det.
	print( celsius )

if __name__ == "__main__":
	fahrenheitToCelsius()