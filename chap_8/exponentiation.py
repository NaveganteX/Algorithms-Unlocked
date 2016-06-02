def exponentiation(x, n):
	def _exp(base, time, accumulate):
		if time is 0:
			return accumulate
		if time%2 is 0:
			return _exp(base*base, int(time/2), accumulate)
		return _exp(base, time-1, base*accumulate)

	return _exp(x, n, 1)

if __name__ == '__main__':
	x = 2
	for i in range(10):
		print("{}^{} =".format(x, i), exponentiation(x, i))