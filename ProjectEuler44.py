import math
import time

def getDiff(pent1, pent2):
	return (pent1 - pent2)

def getSum(pent1, pent2):
	return (pent1 + pent2)

def isPent(pentNum):
	if(((1 + math.sqrt(1 + 24*pentNum)) / 6 ) % 1 == 0):
		return True
	else:
		return False 

smallDiffs = []
pentagonals = []
for i in range(1, 4500):
	pentagonals.append(i*(3*i - 1) / 2)
	for j in range(i - 1, -1, -1):
		if(isPent(getSum(pentagonals[i - 1], pentagonals[j]))):
			if(isPent(getDiff(pentagonals[i - 1], pentagonals[j]))):
				print("BOTH!! Pair is:", pentagonals[i - 1], pentagonals[j])
				smallDiffs.append(getDiff(pentagonals[i - 1], pentagonals[j]))
				break

print(min(smallDiffs))
