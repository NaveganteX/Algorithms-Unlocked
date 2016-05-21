import sys
sys.path.insert(0, '../chap_5')

from dag_shortest_paths import Graph

def bellman_ford(graph, source):
	shortest         = [None] * graph.v_num
	shortest[source] = 0
	pred  = [None] * graph.v_num
	queue = list(range(graph.v_num))

	def _relax(u, v):
		if u == v or shortest[u] is None:
			return
		if shortest[v] is None or shortest[u] + graph.adjacency_matrix[u, v] < shortest[v]:
			shortest[v] = shortest[u] + graph.adjacency_matrix[u, v]
			pred[v] = u

	for _ in range(graph.v_num):
		for i in range(graph.v_num):
			for m in range(graph.v_num):
				if graph.adjacent(i, m):
					_relax(i, m)

	return shortest, pred

def trans(alphabet):
	return {"s":0, "t":1, "x":2, "y":3, "z":4}[alphabet]

if __name__ == '__main__':
	graph = Graph(5)
	graph.adjacency_matrix[trans("s"), trans("t")] = 6
	graph.adjacency_matrix[trans("s"), trans("y")] = 7

	graph.adjacency_matrix[trans("t"), trans("x")] = 5
	graph.adjacency_matrix[trans("t"), trans("y")] = 8
	graph.adjacency_matrix[trans("t"), trans("z")] = -4

	graph.adjacency_matrix[trans("x"), trans("t")] = -2

	graph.adjacency_matrix[trans("y"), trans("x")] = -3
	graph.adjacency_matrix[trans("y"), trans("z")] = 9

	graph.adjacency_matrix[trans("z"), trans("s")] = 2
	graph.adjacency_matrix[trans("z"), trans("x")] = 7

	shortest, pred = bellman_ford(graph, 0)
	print("shortest:", shortest)
	print("pred:    ", pred)