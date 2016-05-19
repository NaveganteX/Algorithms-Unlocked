import sys
sys.path.insert(0, '../chap_5')

from dag_shortest_paths import Graph

def dijkstra(graph, source):
	shortest = [None] * graph.v_num
	shortest[source] = 0
	pred = [None] * graph.v_num
	queue = list(range(graph.v_num))
	weight = graph.adjacency_matrix

	def _relax(u, v):
		if shortest[v] is None or shortest[u] + weight[u, v] < shortest[v]:
			shortest[v] = shortest[u] + weight[u, v]
			pred[v] = u

	while queue:
		lowest_shortest_index = queue[0]
		for v_index in queue:
			if not shortest[lowest_shortest_index] and shortest[v_index]:
				lowest_shortest_index = v_index
			if shortest[v_index] and shortest[v_index] < shortest[lowest_shortest_index]:
				lowest_shortest_index = v_index
		queue.remove(lowest_shortest_index)

		for node in range(graph.v_num):
			if graph.adjacency_matrix[lowest_shortest_index, node]:
				_relax(lowest_shortest_index, node)

	print("shortest:", shortest)
	print("pred:    ", pred)

if __name__ == '__main__':
	graph = Graph(5)
	graph.adjacency_matrix[0, 1] = 6
	graph.adjacency_matrix[0, 3] = 4
	graph.adjacency_matrix[1, 2] = 3
	graph.adjacency_matrix[1, 3] = 2
	graph.adjacency_matrix[2, 4] = 4
	graph.adjacency_matrix[3, 1] = 1
	graph.adjacency_matrix[3, 2] = 9
	graph.adjacency_matrix[3, 4] = 3
	graph.adjacency_matrix[4, 0] = 7
	graph.adjacency_matrix[4, 2] = 5

	dijkstra(graph, 0)