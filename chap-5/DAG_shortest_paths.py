from topological_sort import topological_sort

class Graph(object):
	def __init__(self, num):
		self.v_num = num
		self.adjacency_matrix = { (i, m): None for i in range(self.v_num) for m in range(self.v_num) }

	def generate_adjacency_list(self):
		adjacency_list = []
		for i in range(self.v_num):
			current_reach = []
			for m in range(self.v_num):
				if self.adjacency_matrix[i, m] is not None:
					current_reach += [m]
			adjacency_list += [current_reach]
		return adjacency_list

def DAG_shortest_paths(graph, weight, source):
	v_num = graph.v_num
	pred  = [None] * v_num
	shortest         = [None] * v_num
	shortest[source] = 0

	def _relax(u, v):
		if shortest[v] == None or shortest[u] + weight[u, v] < shortest[v]:
			shortest[v] = shortest[u] + weight[u, v]
			pred[v] = u

	linear_order = topological_sort(graph.generate_adjacency_list())
	for vertex_u in linear_order:
		for v in range(v_num):
			if weight[vertex_u, v]:
				_relax(vertex_u, v)

	print("shortest:", shortest)
	print()
	print("pred:    ", pred)

graph = Graph(6)
graph.adjacency_matrix[0, 1] = 5
graph.adjacency_matrix[0, 2] = 3
graph.adjacency_matrix[1, 2] = 2
graph.adjacency_matrix[1, 3] = 6
graph.adjacency_matrix[2, 3] = 7
graph.adjacency_matrix[2, 4] = 4
graph.adjacency_matrix[2, 5] = 2
graph.adjacency_matrix[3, 4] = -1
graph.adjacency_matrix[3, 5] = 1
graph.adjacency_matrix[4, 5] = -2

DAG_shortest_paths(graph, graph.adjacency_matrix, 0)