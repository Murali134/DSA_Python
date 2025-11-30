def selection_sort(arr):
	n = len(arr)
	for i in range(n-1):
		min_index = i
		for j in range(i+1, n-1):
			if(arr[j] < arr[min_index]):
				min_index = j
				arr[i], arr[min_index] = arr[min_index], arr[i]
	return arr

my_list = [23423, 23, 2423, 425]
print(selection_sort(my_list))

