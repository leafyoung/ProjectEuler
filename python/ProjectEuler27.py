import time

primes = [True for x in range(0, 500000)]

# sieve of erasthones to get primes
for i in range(2, 500000):
	if primes[i] is True:
		mult = 2
		product = i*mult
		while product < 500000:
			primes[product] = False
			mult += 1
			product = i*mult

def isPrime(number):
	if number > 0:
		if primes[number] == True:
			return True
	else:
		return False

# b can only be prime
b = []
for i in range(1, 1001):
	if primes[i]:
		b.append(i)
		b.append(-i)

a = [x for x in range(-999, 1000)]

maxPrimes = 0
aMax = 0
bMax = 0

t = time.time()
for num in a:
	for othernum in b:
		# counts sequential primes generated
		count = 0
		for i in range(0, 100):
			formula = i**2 + num*i + othernum
			if isPrime(formula):
				count += 1
			else:
				if maxPrimes < count:
					aMax = num
					bMax = othernum
					maxPrimes = count
				break

total = time.time() - t
print("Amax=", aMax, "Bmax=", bMax, "maxPrimes=", maxPrimes)
print("Sol found in", total, "s and the product is:", aMax*bMax)
		