sumOfPowers = 0
for i in range(1, 1001):
	number = i**i
	if len(str(number)[0:-2]) < 11:
		sumOfPowers += number
	else:
		sumOfPowers += int(str(number)[-10:])

print(str(sumOfPowers)[-10:])
