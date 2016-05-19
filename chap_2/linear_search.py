def linear_search(array, x):
	answer = -1
	n = len(array)
	for i in range(0, n):
		if array[i] == x:
			answer = i
	return answer

def better_linear_search_range(array, x):
	n = len(array)
	for i in range(0, n):
		if array[i] == x:
			return i
	return -1

def better_linear_search_while(array, x):
	i = 0
	n = len(array)
	while i < n:
		if array[i] == x:
			return i
		i += 1
	return -1

def sentinel_linear_search(array, x):
	n = len(array)
	last_item  = array[n-1]
	array[n-1] = x
	i = 0
	while array[i] != x:
		i += 1
	array[n-1] = last_item
	if i < n-1 or array[n-1] == x:
		return i
	return -1

def recursive_linear_search(array, i, x):
	if i > len(array)-1:
		return -1
	if array[i] == x:
		return i
	return recursive_linear_search(array, i+1, x)

square_array = [x*x for x in range(20000000)]
x = 19271946**2

import cProfile

cProfile.run("better_linear_search_range(square_array, x)")
cProfile.run("better_linear_search_while(square_array, x)")
cProfile.run("sentinel_linear_search(square_array, x)")
#cProfile.run("recursive_linear_search(square_array, n, 0, x)")
# RecursionError: maximum recursion depth exceeded in comparison
