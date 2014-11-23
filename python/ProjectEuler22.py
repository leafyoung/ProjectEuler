names = open("names.txt", "r")
fetchedNames = []
for line in names:
	fetchedNames = line.split(',')

for i in range(0, len(fetchedNames)):
	fetchedNames[i] = fetchedNames[i].strip('\"')


fetchedNames.sort()

listSum = 0

for i in range(0, len(fetchedNames)):
	nameScore = 0
	print("Calculating sum of:", fetchedNames[i])
	for j in range(0, len(fetchedNames[i])):
		nameScore += ord(fetchedNames[i][j]) - 64
		print("Namescore:", nameScore)

	nameScore *= (i + 1)
	listSum += nameScore

print("List Sum:", listSum)

