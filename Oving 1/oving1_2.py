# IT Grunnkurs 2014
# Trond Humborstad
# Øving 1
# Oppgave 2

import math

# Deklarer objektet Kule
class Kule(object):

	radius = 0

	def __init__(self, radius):
		self.radius = radius

	def overflateareal(self):
		'''Beregner overflatearealet til en kule'''
		# Vi tar utgangspunkt i formelen 4πr²
		# Vi bruker også pythons math-modul for å beregne pi og potens
		return 4 * math.pi * math.pow(self.radius, 2)

	def volum(self):
		'''Beregner volum til en kule'''
		# Vi tar utgangspunkt i formelen (4/3)πr³
		return (4/3) * math.pi * math.pow(self.radius, 3)

def main():
	# Vi typecaster inputen til en float
	radius = float(input("Skriv inn radiusen til en kule: "))

	# Oppretter et kuleobjekt
	kuleObjekt = Kule(radius)
	print("Overflaten til kulen er {:.2f}".format(kuleObjekt.overflateareal()))
	print("Volumet til kulen er {:.2f}".format(kuleObjekt.volum()))

if __name__ == "__main__":
	main()