from math import *

def isPentagonal(n):
	return ((1 + sqrt(1 + 24*n)) / 6) % 1 == 0

i = 143
while True:
	i += 1
	hexa = i*(2 * i - 1)

	if isPentagonal(hexa):
		print(hexa)
		break

