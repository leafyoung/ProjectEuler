numbers = []
powersOf5 = [0 for i in range(10)]

for i in range(0, 10):
	powersOf5[i] = pow(i, 5)


for i in range(2, 1000000):
	number = []
	digitSum = 0
	for digits in str(i):
		number.append(digits)

	for digit in number:
		if powersOf5[int(digit)] > i:
			break
		else:
			digitSum += powersOf5[int(digit)]

	if digitSum == i:
		numbers.append(i)

total = 0
for x in numbers:
	total += x

print("Total:", total)
