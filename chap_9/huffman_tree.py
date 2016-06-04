class TreeNode(object):
	def __init__(self, char, freq, left=None, right=None):
		self.char = char
		self.freq = freq
		self.code = ""
		self.left  = left
		self.right = right

	def get_code_table(self):
		code_table = {}
		def _iter(node):
			if node.is_leaf():
				code_table[node.char] = node.code
			if node.left:
				_iter(node.left)
			if node.right:
				_iter(node.right)

		_iter(self)
		return code_table

	def is_leaf(self):
		return (not self.left) and (not self.right)

	def print_self(self, indent):
		print(indent, end="")
		print(self.char, "-", self.freq, "-", self.code)

	def visit(self, indent=""):
		self.print_self(indent)
		indent += "   "
		if self.left:
			self.left.visit(indent)
		if self.right:
			self.right.visit(indent)

def count_freq(text):
	char = [c for c in set(text)]
	freq = [text.count(c)/len(text) for c in char]
	return char, freq

def build_huffman_tree(char, freq):
	assert(len(char) is len(freq))

	queue = [TreeNode(char[i], freq[i]) for i in range(len(char))]
	for i in range(len(char)-1):
		queue.sort(key=lambda x: x.freq)
		x, y  = queue[0:2]
		queue = queue[2:]
		z_node = TreeNode(x.char+y.char, x.freq+y.freq, x, y)
		queue += [z_node]
	assert(len(queue) is 1)
	return queue[0]

def huffman_set_code(tree_node, prefix=""):
	tree_node.code = prefix
	if tree_node.left:
		huffman_set_code(tree_node.left,  prefix+"0")
	if tree_node.right:
		huffman_set_code(tree_node.right, prefix+"1")

def huffman_encode(code_table, text, code=""):
	if not text:
		return code
	return huffman_encode(code_table, text[1:], code+code_table[text[0]])

def huffman_decode(root, code):
	def _decode(node, i=0):
		if node.is_leaf():
			return node.char, i
		if code[i] == "0":
			return _decode(node.left,  i+1)
		if code[i] == "1":
			return _decode(node.right, i+1)
		raise ValueError('Illegal code')

	text = ""
	while code:
		char, step = _decode(root)
		code, text = code[step:], text+char

	return text

if __name__ == '__main__':
	text = "TAATTAGAAATTCTATTATA"
	char, freq = count_freq(text)
	root = build_huffman_tree(char, freq)
	huffman_set_code(root)
	print("Huffman tree:")
	root.visit()
	print()
	print("Code table:")
	print(root.get_code_table())
	print()
	print("Text:  ", text)
	huffman_code = huffman_encode(root.get_code_table(), text)
	print("Encode:", huffman_code)
	print("Decode:", huffman_decode(root, huffman_code))