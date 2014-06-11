import itertools
import functools
import time
from math import *
# FUCKING FAST PRIME FUNCTION
def isPrime(n):
	if n % 2 == 0 or n % 3 == 0:
		return False

	x = int(sqrt(n))
	i = 1
	while (6*i - 1) <= x:
		if (n % (6*i - 1)) == 0:
			return False

		if (n % (6*i + 1)) == 0:
			return False

		i += 1

	return True

t = time.time()
for i in range(1000, 4500):
	if isPrime(i):	
		prime_list = []
		# grabs list of prime permutations of each number
		for perm in itertools.permutations(str(i)):
			# cute functions to turn a tuple->string->int
			perm_int = int(functools.reduce(lambda rst, d: rst + d, perm))
			if isPrime(perm_int) and perm_int > 1000 and (perm_int not in prime_list):
				prime_list.append(perm_int)
		
		# only checks lists with more than 3 terms
		if (len(prime_list) > 2):
			for i in range(0, len(prime_list) - 2):
					for j in range(i + 1, len(prime_list) - 1):
							for k in range(j + 1, len(prime_list)):
								if prime_list[k] - prime_list[j] == prime_list[j] - prime_list[i]:
									print(prime_list[i], prime_list[j], prime_list[k])
									break


print(time.time() - t)


