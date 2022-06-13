def sorting(data):
	for k in range(len(data) - 1):
		min_idx = k
		for i in range(k+1, len(data)):
			if data[i] < data[min_idx]:
				min_idx = i
		#data[k], data[min_idx] = data[min_idx], data[k]
		aux = data[k]
		data[k] = data[min_idx]
		data[min_idx] = aux
	return data


data = [10, 2, 5, 1, 7, 823, 23, 6]
print(sorting(data))
data = [34, 51, 5234, 56, 12, 2, 5, 1, 32, 2, 3, 5]
print(sorting(data))
