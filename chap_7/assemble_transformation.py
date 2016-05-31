from compute_transform_tables import compute_transform_tables, print_op_table

def assemble_transformation(op_table, x_len, y_len):
	def _assemble_transformation(i, k):
		def __is_copy():    return "copy" in op_table[i, k]
		def __is_replace(): return "rep"  in op_table[i, k]
		def __is_delete():  return "del"  in op_table[i, k]
		def __is_insert():  return "ins"  in op_table[i, k]

		if i is -1 and k is -1:
			return []
		if __is_copy() or __is_replace():
			return _assemble_transformation(i-1, k-1) + [op_table[i, k]]
		if __is_delete():
			return _assemble_transformation(i-1, k)   + [op_table[i, k]]
		if __is_insert():
			return _assemble_transformation(i, k-1)   + [op_table[i, k]]

		raise ValueError('Unknown operation')

	return _assemble_transformation(x_len-1, y_len-1)

if __name__ == '__main__':
	y_str = "CCGT"
	x_str = "ACAAGC"
	_, op_table = compute_transform_tables(x_str, y_str)
	print("Operation table:")
	print_op_table(op_table, x_str, y_str)

	print()
	print("Operation sequence:")
	print(assemble_transformation(op_table, len(x_str), len(y_str)))