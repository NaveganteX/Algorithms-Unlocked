def counting_sort(array, lower, upper):
	n = len(array)
	m = upper-lower+1

	equal_array = [0]*m
	for i in range(0, n):
		equal_array[array[i]] += 1

	sorted_array =[]
	for i in range(0, m):
		sorted_array += [i]*equal_array[i]
	return sorted_array

lower = 0
upper = 10
from random import randint

test_array = [randint(lower, upper) for _ in range(25)]

print("before:       ", test_array)
print("counting_sort:", counting_sort(test_array, lower, upper))