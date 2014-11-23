def isLeapYear(year):
	if (year % 4 == 0 and year % 100 != 0):
		return 1
	elif (year % 400 == 0):
		return 1
	else:
		return 0

months = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
countSundays = 0
currentDay = 2

for x in range(1901, 2001):
	if isLeapYear(x):
		months[1] = 29
	else:
		months[1] = 28

	print("Year:", x, "LeapYear:", months[1])

	for y in range(len(months)):
		dayOfMonth = 1
		for z in range(months[y]):
			if currentDay % 7 == 0 and dayOfMonth == 1:
				countSundays += 1
				print("Count Sundays + 1")

			currentDay += 1
			dayOfMonth += 1

		print("Next Month")

print("Count of Sundays:", countSundays)