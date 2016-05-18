def topological_sort(graph):
	in_degree = [0] * len(graph)
	for item in graph:
		for out_vertex in item:
			in_degree[out_vertex] += 1

	next_list = []
	for i in range(len(in_degree)):
		if in_degree[i] == 0:
			next_list += [i]

	topological_order = []
	while next_list:
		new_item  = next_list[0]
		next_list = next_list[1:]
		topological_order += [new_item];
		for index in graph[new_item]:
			in_degree[index] -= 1
			if in_degree[index] == 0:
				next_list += [index]

	return topological_order

if __name__ == '__main__':
	adjacency_list = [
		[2],
		[3],
		[3, 4],
		[5],
		[5],
		[6, 10],
		[7],
		[12],
		[9],
		[10],
		[11],
		[12],
		[13],
		[]
	]

	print(topological_sort(adjacency_list))