import time
t = time.time()

combinations = 0
coins = [ 200, 100, 50, 20, 10, 5, 2, 1 ]

total = 0
for i in range(0, 2):
	for j in range(0, 3):
		for k in range(0, 5):
			for l in range(0, 11):
				for m in range(0, 21):
					for n in range(0, 41):
						for o in range(0, 101):
							for p in range(0, 201):
								total = i*200 + j*100 + k*50 + l*20 + m*10 + n*5 + o*2 + p*1
								if total == 200:
									combinations += 1
								elif total > 200:
									break


print(combinations, time.time() - t)