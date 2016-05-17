def get_min_index(array):
	min_var = array[0]
	index   = 0
	for i in range(1, len(array)):
		if array[i] < min_var:
			min_var = array[i]
			index   = i
	return index

def selection_sort_0(array):
	for i in range(0, len(array)-1):
		min_index = get_min_index(array[i:]) + i
		array[i], array[min_index] = array[min_index], array[i]

def selection_sort_1(array):
	for i in range(0, len(array)-1):
		min_index = i
		for m in range(i+1, len(array)):
			if array[m] < array[min_index]:
				min_index = m
		array[i], array[min_index] = array[min_index], array[i]


from random import shuffle

test_array = [i for i in range(20)]

shuffle(test_array)
print("before:          ", test_array)
selection_sort_0(test_array)
print("selection_sort_0:", test_array, "\n")

shuffle(test_array)
print("before:          ", test_array)
selection_sort_1(test_array)
print("selection_sort_1:", test_array)