def fa_string_matcher(text, next_state, m):
	state = 0
	for i in range(len(text)):
		state = next_state[state, text[i]]
		if state is m:
			print("Pattern occurs with shift", i-m+1)
			print(text[i-m+1:])

if __name__ == '__main__':
	text    = "GTAACAGTAAACG"
	pattern = "AAC"

	next_state = {}
	for i in range(len(set(text))):
		for char in set(text):
			next_state[i, char] = 0

	next_state[0, "A"] = 1

	next_state[1, "A"] = 2

	next_state[2, "A"] = 2
	next_state[2, "C"] = 3

	next_state[3, "A"] = 1

	print("Text:   ", text)
	print("Pattern:", pattern)
	print()
	fa_string_matcher(text, next_state, len(pattern))