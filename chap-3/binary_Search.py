def binary_search(array, x):
	p = 0
	r = len(array)-1
	while p <= r:
		q = int((p+r)/2)
		if array[q] == x:
			return q
		elif array[q] > x:
			r = q-1
		else:
			p = q+1
	return -1

def recursive_binary_search(array, x):
	def _recursive_binary_search(p, r):
		if p > r:
			return -1
		q = int((p+r)/2)
		if array[q] == x:
			return q
		elif array[q] > x:
			return _recursive_binary_search(p, q-1)
		else:
			return _recursive_binary_search(q+1, r)

	return _recursive_binary_search(0, len(square_array)-1)


square_array = [x*x for x in range(2000000)]
x = 1972946**2+1

print(binary_search(square_array, x))
print(recursive_binary_search(square_array, x))