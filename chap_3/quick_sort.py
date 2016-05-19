def deterministic_quicksort(array):
	def _deterministic_quick_sort(p, r):
		if p >= r: return
		q = _deterministic_partion(p, r)
		_deterministic_quick_sort(p, q-1)
		_deterministic_quick_sort(q+1, r)

	def _deterministic_partion(p, r):
		pivot = array[r]
		i = p
		for j in range(p, r):
			if array[j] < pivot:
				array[i], array[j] = array[j], array[i]
				i += 1
		array[i], array[r] = array[r], array[i]
		return i

	_deterministic_quick_sort(0, len(array)-1)

from random import randint

def randomized_quicksort(array):
	def _randomized_quick_sort(p, r):
		if p >= r: return
		q = _randomized_partion(p, r)
		_randomized_quick_sort(p, q-1)
		_randomized_quick_sort(q+1, r)

	def _randomized_partion(p, r):
		random_pivot_index = randint(p, r)
		array[random_pivot_index], array[r] = array[r], array[random_pivot_index]
		pivot = array[r]
		i = p
		for j in range(p, r):
			if array[j] < pivot:
				array[i], array[j] = array[j], array[i]
				i += 1
		array[i], array[r] = array[r], array[i]
		return i

	_randomized_quick_sort(0, len(array)-1)


from random import shuffle

test_array = [i for i in range(20)]

import cProfile

#cProfile.run("better_linear_search_range(square_array, x)")


shuffle(test_array)
print("before:                 ", test_array)
deterministic_quicksort(test_array)
print("deterministic_quicksort:", test_array)

print()

shuffle(test_array)
print("before:                 ", test_array)
randomized_quicksort(test_array)
print("randomized_quicksort:   ", test_array)