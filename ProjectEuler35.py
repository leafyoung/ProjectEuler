from collections import deque
import time

numbers = list(True for i in range(1000001))
primes = []

for i in range(2, int(len(numbers) / 2)):
	if numbers[i]:
		for j in range(i*2, len(numbers), i):
			numbers[j] = False
		
for i in range(len(numbers)):
	if numbers[i]:
		primes.append(i)

t = time.time()
circ_count = 0
for i in range(2, len(primes)):
	numDigits = deque(int(digit) for digit in str(primes[i]))
	
	possible_circ = True
	for num in numDigits:
		if (num % 2 == 0 or num % 5 == 0 or num == 0) and num != 5 and num != 2:
			possible_circ = False
			break

	if possible_circ:
		circ_prime = True	
		if len(numDigits) != 1:
			count = 1
			while count < len(numDigits):
				numDigits.appendleft(numDigits.pop())
				rotation = int("".join(str(char) for char in numDigits))

				if rotation not in primes:
					circ_prime = False
					break

				count += 1

		if circ_prime:
			circ_count += 1

print(circ_count)
print(time.time() - t, "s")




