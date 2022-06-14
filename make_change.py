def make_change(value):
	coins = {100: 0, 50: 0, 20: 0, 10: 0, 2: 0, 1: 0}
	for c in coins.keys():
		coins[c] = value // c
		value %= c

	return coins



print(make_change(24)) # 20p 2p 2p
print(make_change(163)) # 1 50p 10p 2p 1p
