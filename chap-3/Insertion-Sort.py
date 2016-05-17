def insertion_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		m = i-1
		while m>-1 and array[m]>key:
			array[m+1] = array[m]
			m -= 1
		array[m+1] = key

from random import shuffle

test_array = [i for i in range(20)]
shuffle(test_array)

print("before:        ", test_array)
insertion_sort(test_array)
print("insertion_sort:", test_array)