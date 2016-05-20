def max_heapify(array, index):
	heap_size = len(array)
	left_index  = 2 * index +1
	right_index = left_index + 1

	if left_index < heap_size and array[left_index]>array[index]:
		largest = left_index
	else:
		largest = index

	if right_index < heap_size and array[right_index]>array[largest]:
		largest = right_index

	if largest is not index:
		array[index], array[largest] = array[largest], array[index]
		max_heapify(array, largest)

def build_max_heap(array):
	for i in reversed(range(0, int(len(array)/2))):
		max_heapify(array, i)

def heap_extract_max(array):
	max_so_far = array[0]
	array[0] = array[len(array)-1]
	max_heapify(array, 0)
	del array[-1]
	return max_so_far

test_array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print("before:      ", test_array)

build_max_heap(test_array)
print("heap_array:  ", test_array)

sorted_array = []
while test_array:
	max_item = heap_extract_max(test_array)
	sorted_array += [max_item]
print("sorted_array:", sorted_array)