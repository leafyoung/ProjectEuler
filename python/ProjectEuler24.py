import math

perm = input("Which lexicographic permutation of the digits 0 1 2 3 4 5 6 7 8 9 do you want: ")
perm = int(perm) - 1

digitList = []
nums = [x for x in range(0, 10)]

for i in range(9, 0, -1):
	print("i=", i)
	if perm != 0:
		num = int(perm / math.factorial(i)) 
		digitList.append(nums[num])
		nums.remove(nums[num])
		perm = perm % math.factorial(i)
	else:
		break

	print("Incomplete factorial:", digitList)
	print("Nums Left:", nums)

for num in nums:
	digitList.append(num)

print(digitList)