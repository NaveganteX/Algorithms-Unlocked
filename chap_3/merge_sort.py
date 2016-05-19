def merge_sort(array):
	def _merge_sort(p, r):
		if p >= r-1: return
		q = int((p+r)/2)
		_merge_sort(p, q)
		_merge_sort(q, r)
		_merge(p, q, r)

	def _merge(p, q, r):
		array_0 = array[p:q]
		array_1 = array[q:r]
		merged_array = []
		while array_0 and array_1:
			if array_0[0] < array_1[0]:
				merged_array += [array_0[0]]
				array_0 = array_0[1:]
			else:
				merged_array += [array_1[0]]
				array_1 = array_1[1:]
		merged_array += array_0 + array_1
		array[p:r] = merged_array

	_merge_sort(0, len(array))

from random import shuffle

test_array = [i for i in range(20)]
shuffle(test_array)

print("before    :", test_array)
merge_sort(test_array)
print("merge_sort:", test_array)