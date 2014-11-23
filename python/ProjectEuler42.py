import time

fileInput = open("words.txt", "r")

words = []
for line in fileInput:
	words = line.split(',')

for i in range(0, len(words)):
	words[i] = words[i].strip('\"')

# creates list of triangle numbers t = 1/2n(n+1)
triangle_nums = [ int(.5*i*(i + 1)) for i in range(1, 100)]

triangle_word_count = 0

t = time.time()

for word in words:
	word_sum = 0

	for letter in word:
		letterVal = ord(letter) - 64
		word_sum += letterVal

	for num in triangle_nums:
		if word_sum == num:
			triangle_word_count += 1
			break

print("Number of triangle words: " + str(triangle_word_count))
print("Time to run: " + str(time.time() - t) + "s")