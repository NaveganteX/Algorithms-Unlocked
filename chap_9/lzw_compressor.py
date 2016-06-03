import string

def gen_ASCII_table():
	ASCII_table = {}
	for char in string.ascii_uppercase:
		ASCII_table[ord(char)] = char

	size = 256
	# initialze ASCII character set with bare alphabet
	return ASCII_table, size

def lzw_compressor(text):
	code_dict, next_socket = gen_ASCII_table()

	def _get_index(s):
		for item in code_dict:
			if code_dict[item] == s:
				return item

	code_sequence = []
	s, text = text[0], text[1:]
	while text:
		c, text = text[0], text[1:]
		if _get_index(s+c):
			s = s+c
		else:
			code_sequence += [_get_index(s)]
			code_dict[next_socket] = s+c
			next_socket += 1
			s = c
	code_sequence += [_get_index(s)]

	return code_sequence

if __name__ == '__main__':
	text = "TATAGATCTTAATATA"

	print("Text  :", text)
	print("Encode:", lzw_compressor(text))