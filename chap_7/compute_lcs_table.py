def compute_lcs_table(x_str, y_str):
	x_len = len(x_str)
	y_len = len(y_str)
	lcs_table = {}

	for i in range(-1, x_len):
		lcs_table[i, -1] = 0
	for k in range(-1, y_len):
		lcs_table[-1, k] = 0

	for i in range(x_len):
		for k in range(y_len):
			if x_str[i] == y_str[k]:
				lcs_table[i, k] = lcs_table[i-1, k-1] + 1
			else:
				lcs_table[i, k] = max(lcs_table[i-1, k], lcs_table[i, k-1])
	return lcs_table

def print_table(table, x_str, y_str):
	print(end="    ")
	for char in y_str:
		print(char, end=" ")
	print()

	for i in range(-1, len(x_str)):
		if i >= 0:
			print(x_str[i], end=" ")
		else:
			print(end="  ")
		for k in range(-1, len(y_str)):
			print(table[i, k], end=" ")
		print()

if __name__ == '__main__':
	x_str = "CATCGA"
	y_str = "GTACCGTCA"
	print_table(compute_lcs_table(x_str, y_str), x_str, y_str)