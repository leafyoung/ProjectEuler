import itertools 
from itertools import repeat
import time

sizeOfGrid = int(input("Please enter the size of the grid: ")) 

t= time.time()

grid = [[0 for x in range(sizeOfGrid + 1)] for y in range(sizeOfGrid + 1)]
for i in range(0, sizeOfGrid + 1):
	grid[i][sizeOfGrid] = 1
	grid[sizeOfGrid][i] = 1

for i in range(sizeOfGrid - 1, -1, -1):
	for j in range(sizeOfGrid - 1, -1, -1):
		grid[i][j] = grid[i][j + 1] + grid[i + 1][j]

print("Num of paths:", grid[0][0], "Time:", time.time() - t)
