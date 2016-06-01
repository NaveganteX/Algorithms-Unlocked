def fa_string_matcher(text, next_state, m):
	print("raw text:", text)
	state = 0
	for i in range(len(text)):
		state = next_state[state, text[i]]
		if state is m:
			print("Pattern occurs with shift", i-m+1)
			print(text[i-m+1:])

if __name__ == '__main__':
	temp_text    = "GTAACAGTAAACG"
	pattern = "AAC"

	temp_next_state = {}
	for i in range(len(set(temp_text))):
		for char in set(temp_text):
			temp_next_state[i, char] = 0

	temp_next_state[0, "A"] = 1

	temp_next_state[1, "A"] = 2

	temp_next_state[2, "A"] = 2
	temp_next_state[2, "C"] = 3

	temp_next_state[3, "A"] = 1

	fa_string_matcher(temp_text, temp_next_state, len(pattern))