pan_prods = []

for i in range(2, 100):
	for j in range(100, 9999):
		product = i * j

		if product < 10000:
			all_nums = str(i) + str(j) + str(product)

			no_zero = True
			for char in all_nums:
				if char == '0':
					no_zero = False
					break

			if no_zero and len(all_nums) == 9:
				pandigital = True
				for k in range(0, 8):
					for m in range(k + 1, 9):
						if(all_nums[k] == all_nums[m]):
							pandigital = False
							k = 8
							break

				if pandigital:
					print("Pandigital", all_nums)
					in_list = False
					if product in pan_prods:
						in_list = True
						break

					if not in_list:
						print("Appending", product, "Pandigital:", all_nums)
						pan_prods.append(product)
		else:
			break

print(sum(pan_prods))

