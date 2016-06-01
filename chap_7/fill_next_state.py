from fa_string_matcher import fa_string_matcher

def fill_next_state_table(set_of_text, pattern):
	next_state = {}
	for k in range(len(pattern)+1):
		for char in set_of_text:
			P_suffix_with_char = pattern[:k]+char
			i = min(len(P_suffix_with_char), len(pattern))
			while not P_suffix_with_char.endswith(pattern[:i]):
				i -= 1
			next_state[k, char] = i
	return next_state

def print_next_state_table(next_state, pattern, set_of_text):
	print("Pattern =", pattern)

	print(" "*3, end="")
	for char in set_of_text:
		print(char, end=" ")
	print()
	for i in range(len(pattern)+1):
		print("{}:".format(i), end=" ")
		for char in set_of_text:
			print(next_state[i, char], end=" ")
		print()

if __name__ == '__main__':

	pattern     = "ACACAGA"
	set_of_text = "ACGT"
	next_state  = fill_next_state_table(set_of_text, pattern)

	print_next_state_table(next_state, pattern, set_of_text)