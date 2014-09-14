# Øving 3 - Oppgave 2
debug = True

def add(integerOne, integerTwo):
	if debug:
		print("Tallene som summeres er", integerOne, "og", integerTwo)
	print(integerOne + integerTwo)

if __name__ == "__main__":
	add(7, 4)