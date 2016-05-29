from compute_lcs_table import compute_lcs_table, print_table

def assemble_lcs(x_str, y_str, lcs_table):
	def _assemble_lcs(i, k, lcs):
		if lcs_table[i, k] is 0:
			return lcs
		if x_str[i] == y_str[k]:
			return _assemble_lcs(i-1, k-1, x_str[i]+lcs)
		else:
			if lcs_table[i, k-1] > lcs_table[i-1, k]:
				return _assemble_lcs(i, k-1, lcs)
			else:
				return _assemble_lcs(i-1, k, lcs)

	return _assemble_lcs(len(x_str)-1, len(y_str)-1, "")

if __name__ == '__main__':
	x_str = "CATCGA"
	y_str = "GTACCGTCA"
	lcs_table = compute_lcs_table(x_str, y_str)
	print_table(lcs_table, x_str, y_str)
	print()
	print("lcs:", assemble_lcs(x_str, y_str, lcs_table))