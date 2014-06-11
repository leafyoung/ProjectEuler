from math import *
import time
#from bitarray import bitarray

def ESieveBits(upperLimit):
	# will only allocate enough space in the bit array for odd numbers and 2
	sieveBound = int(upperLimit - 1) / 2;
	# only checks numbers up until the upperLimit's sqrt
	upperSqrt = (int(sqrt(upperLimit) - 1) / 2)

	prime_bits = bitarray(upperLimit)
	prime_bits[:] = True
	
	for i in range(upperSqrt + 1):
		if prime_bits[i]:
			# only checks the next odd past double i
			for j in range(i*2*(i+1), sieveBound, 2*i+1):
				clearBit(prime_bits, j)

def ESieve(upperLimit):
	# will only allocate enough space in the bit array for odd numbers and 2
	sieveBound = int(int(upperLimit - 1) / 2);
	# only checks numbers up until the upperLimit's sqrt
	upperSqrt = int((int(sqrt(upperLimit)) - 1) / 2)

	prime_bools = [True for x in range(sieveBound + 1)]
	for i in range(1, upperSqrt + 1):
		if prime_bools[i]:
			for j in range(i * 2 * (i + 1), sieveBound + 1, 2*i+1):
				prime_bools[j] = False

	primes = []
	primes.append(2)
	for i in range(1, sieveBound + 1):
		if prime_bools[i]:
			primes.append(2*i+1)

	return primes

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

limit = 1000000
primes = ESieve(limit)
largest_seq = 0
prime = 0
t = time.time()
for i in range(0, len(primes) - largest_seq):
	prime_sum = 0
	for j in range(i, len(primes)):
		if prime_sum < limit:
			prime_sum += primes[j]
			if isPrime(prime_sum) and j - i + 1 > largest_seq:
				largest_seq = j - i + 1
				print(largest_seq, "is largest_seq with sum", prime_sum)
				prime = prime_sum
		else:
			break

print(largest_seq, prime)
print(time.time() - t)
