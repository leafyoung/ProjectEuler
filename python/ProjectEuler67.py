def r_enumerate(container):
    i = len(container)
    for item in reversed(container):
        i -= 1
        yield i, item

if __name__ == '__main__':
	with open ('triangle.txt', 'r') as file_data:
		triangle = [[int(x) for x in line.strip().split()] for line in file_data]
		# iterate starting at the 2nd to last row of the triangle, backwards
		for i, row in r_enumerate(triangle[:-1]):
			print(len(triangle), len(row))
			for j, num in enumerate(row):
				print(i, j)
				if triangle[i+1][j] > triangle[i+1][j+1]:
					triangle[i][j] += triangle[i+1][j]
				else:
					triangle[i][j] += triangle[i+1][j+1]

		print(triangle[0][0])
