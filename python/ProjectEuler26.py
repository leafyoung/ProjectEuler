from decimal import *
import time

getcontext().prec = 10000
fractions = [str(Decimal(Decimal(1) / Decimal(x)))[2:] for x in range(2, 1000)]

longest_cycle = 0
d = 0
t = time.time()
for i in range(len(fractions)):
	if i % 2 != 0:
		count = 0
		while fractions[i][0] == '0':
			fractions[i] = fractions[i][1:]

		if len(fractions[i]) == 10000:
			cycle_length = 0
			for j in range(1, 5001):
				if fractions[i][0:j] == fractions[i][j:j+j]:
					cycle_length = j
					break

			if cycle_length > longest_cycle:
				longest_cycle = cycle_length
				d = i + 2

print("The longest is 1 /", d, "taking", (time.time() - t), "seconds")




