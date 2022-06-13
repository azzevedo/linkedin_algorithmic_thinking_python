import time


def p_doors(doors):
	for d in doors:
		if d:
			print('\033[0;32m1\033[0m', end=' ')
		else:
			print('\033[0;31m0\033[0m', end=' ')
	print('\n' * 3)




doors = [0 for i in range(1, 101)]

#1, #2, #3, #4, #5
c = 1
while c < 101:
    for i in range(c, 101, c):
		p_doors(doors)
        doors[i-1] = not doors[i-1]
		#os.system('cls')
		time.sleep(0.20)
    c += 1


p_doors(doors)
