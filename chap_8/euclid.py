def euclid(a, b):
	if b is 0:
		return a, 1, 0
	g, _i, _k = euclid(b, a%b)
	i = _k
	k = _i - int(a/b) * _k
	return g, i, k

def print_euclid(a, b, g, i, k):
	int_len = lambda x: len(str(x))
	print("{:>{w0}} = {:>{w1}} * {:>{w2}} + {:>{w3}} * {:>{w4}}".format("g", "a", "i", "b", "k", w0=int_len(g), w1=int_len(a), w2=int_len(i), w3=int_len(b), w4=int_len(k)))

	print(g, "=", a, "*", i, "+", b, "*", k)

if __name__ == '__main__':
	a = 432
	b = 128

	g, i, k = euclid(a, b)
	print_euclid(a, b, g, i, k)