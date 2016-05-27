import sys
sys.path.insert(0, '../chap_5')

from dag_shortest_paths import Graph

def dijkstra(graph, source):
	shortest         = [float("inf")] * graph.v_num
	shortest[source] = 0
	pred  = [None] * graph.v_num
	queue = list(range(graph.v_num))

	def _relax(u, v):
		if shortest[u] + graph.adjacency_matrix[u, v] < shortest[v]:
			shortest[v] = shortest[u] + graph.adjacency_matrix[u, v]
			pred[v] = u

	while queue:
		lowest_shortest_index = queue[0]
		for v_index in queue:
			if shortest[v_index] < shortest[lowest_shortest_index]:
				lowest_shortest_index = v_index
		queue.remove(lowest_shortest_index)

		for node in range(graph.v_num):
			_relax(lowest_shortest_index, node)

	return shortest, pred

def trans(alphabet):
	return {"s":0, "t":1, "x":2, "y":3, "z":4}[alphabet]

if __name__ == '__main__':
	graph = Graph(5)
	graph.adjacency_matrix[trans("s"), trans("t")] = 6
	graph.adjacency_matrix[trans("s"), trans("y")] = 4

	graph.adjacency_matrix[trans("t"), trans("x")] = 3
	graph.adjacency_matrix[trans("t"), trans("y")] = 2

	graph.adjacency_matrix[trans("x"), trans("z")] = 4

	graph.adjacency_matrix[trans("y"), trans("t")] = 1
	graph.adjacency_matrix[trans("y"), trans("x")] = 9
	graph.adjacency_matrix[trans("y"), trans("z")] = 3

	graph.adjacency_matrix[trans("z"), trans("s")] = 7
	graph.adjacency_matrix[trans("z"), trans("x")] = 5

	shortest, pred = dijkstra(graph, trans("s"))
	print("shortest:", shortest)
	print("pred:    ", pred)