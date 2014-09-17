# IT Grunnkurs 2014
# Trond Humborstad
# Øving 1
# Oppgave 3

import math

def beregn_volum(radius):
	'''Beregner volum til en kule'''
	# Vi tar utgangspunkt i formelen (4/3)πr³
	volum = (4/3) * math.pi * math.pow(radius, 3)
	print("Volumet til kulen med radius", radius, "er", "{:.2f}".format( volum ))

def main():
	valuesToCalculate = [2.5, 5.0, 7.5]

	for value in valuesToCalculate:
		beregn_volum(value)

if __name__ == "__main__":
	main()