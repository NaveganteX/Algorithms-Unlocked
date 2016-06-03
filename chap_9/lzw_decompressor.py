from lzw_compressor import gen_ASCII_table, lzw_compressor

def lzw_decompressor(indices):
	code_dict, next_socket = gen_ASCII_table()

	decode_sequence = ""

	current, indices = indices[0], indices[1:]
	decode_sequence += code_dict[current]
	while indices:
		previous, current, indices = current, indices[0], indices[1:]

		if current in code_dict:
			s = code_dict[current]
			code_dict[next_socket] = code_dict[previous]+s[0]
		else:
			s = code_dict[previous]+code_dict[previous][0]
			code_dict[next_socket] = s
		decode_sequence += s
		next_socket += 1
	return decode_sequence

if __name__ == '__main__':
	text = "TATAGATCTTAATATA"
	print("Text  :", text)
	indices = lzw_compressor(text)
	print("Encode:", indices)
	print("Decode:", end=" ")
	print(lzw_decompressor(indices))