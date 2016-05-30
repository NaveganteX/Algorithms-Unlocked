def compute_transform_tables(x_str, y_str, c_copy=-1, c_replace=1, c_delete=2, c_insert=2):
	x_len = len(x_str)
	y_len = len(y_str)
	cost_table = {}
	op_table   = {}
	for i in range(x_len):
		cost_table[i, -1] = (i+1)*c_delete
		op_table[i, -1]   = "del-" + x_str[i]
	for k in range(y_len):
		cost_table[-1, k] = (k+1)*c_insert
		op_table[-1, k]   = "ins-" + y_str[k]

	cost_table[-1, -1] = 0
	op_table[-1, -1]   = "$"

	for i in range(x_len):
		for k in range(y_len):
			if x_str[i] == y_str[k]:
				cost_table[i, k] = cost_table[i-1, k-1] + c_copy
				op_table[i, k]   = "copy-" + x_str[i]
			else:
				cost_table[i, k] = cost_table[i-1, k-1] + c_replace
				op_table[i, k]   = "rep-" + x_str[i] + "-" + y_str[k]

			if cost_table[i-1, k] + c_delete < cost_table[i, k]:
				cost_table[i, k] = cost_table[i-1, k] + c_delete
				op_table[i, k]   = "del-" + x_str[i]
			if cost_table[i, k-1] + c_insert < cost_table[i, k]:
				cost_table[i, k] = cost_table[i, k-1] + c_insert
				op_table[i, k]   = "ins-" + y_str[k]
	return cost_table, op_table

def print_op_table(table, x_str, y_str):
	max_length = len(max([table[item] for item in table], key=len))

	print(end=" "*(max_length+5))
	for char in y_str:
		print(char, end=" "*max_length)
	print()

	space_count = 3
	for i in range(-1, len(x_str)):
		if i >= 0:
			print(x_str[i], end=" "*space_count)
		else:
			print(end=" "*(space_count+1))
		for k in range(-1, len(y_str)):
			print("{:<{width}}".format(table[i, k], width=max_length), end=" ")
		print()


from compute_lcs_table import print_table

if __name__ == '__main__':
	y_str = "CCGT"
	x_str = "ACAAGC"
	cost_table, op_table = compute_transform_tables(x_str, y_str)
	print("Cost table:")
	print_table(cost_table, x_str, y_str)

	print()
	print("Operation table:")
	print_op_table(op_table, x_str, y_str)