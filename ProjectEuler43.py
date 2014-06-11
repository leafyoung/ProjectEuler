import itertools 

# This one was difficult

my_list = "0123456789"
primes = [ 2, 3, 5, 7, 11, 13, 17]

perm_sum = 0
for perm in itertools.permutations(my_list):
		perm_str = ''.join(perm)
		if int(perm_str[0]) != 0:
			has_prop = True
			for i in range(1, 8):
				if i == 7 and int(perm_str[7:]) % primes[i - 1] != 0:
					has_prop = False
					break
				elif int(perm_str[i:i+3]) % primes[i - 1] != 0:
					has_prop = False
					break

			if has_prop:
				print(perm_str)
				perm_sum += int(perm_str)


print("perm sum =", perm_sum)
