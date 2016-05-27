import sys
sys.path.insert(0, '../chap_5')

from dag_shortest_paths import Graph
from bellman_ford import bellman_ford

def find_negative_weight_cycle(graph):
	suspect_edge = set()
	cycle = set()
	for i in range(graph.v_num):
		shortest, pred = bellman_ford(graph, i)
		for m in range(graph.v_num):
			for k in range(graph.v_num):
				if shortest[m]+graph.adjacency_matrix[m, k]<shortest[k]:
					suspect_edge.add((m, k))

	for (u, v) in suspect_edge:
		visited = [False] * graph.v_num
		x = v
		while visited[x] is False:
			visited[x] = True
			x = pred[x]
		v = pred[x]
		sub_cycle = [x]
		while v != x:
			sub_cycle = [v] + sub_cycle
			v = pred[v]
		cycle.add(tuple(sub_cycle))

	return cycle

def trans(alphabet):
	return {"s":0, "t":1, "x":2, "y":3, "z":4}[alphabet]

if __name__ == '__main__':

	graph_0 = Graph(5)
	graph_0.adjacency_matrix[trans("s"), trans("t")] = 6
	graph_0.adjacency_matrix[trans("s"), trans("y")] = 7

	graph_0.adjacency_matrix[trans("t"), trans("x")] = -3
	graph_0.adjacency_matrix[trans("t"), trans("y")] = 8
	graph_0.adjacency_matrix[trans("t"), trans("z")] = 4

	graph_0.adjacency_matrix[trans("x"), trans("t")] = -2

	graph_0.adjacency_matrix[trans("y"), trans("x")] = 3
	graph_0.adjacency_matrix[trans("y"), trans("z")] = 9

	graph_0.adjacency_matrix[trans("z"), trans("s")] = 2
	graph_0.adjacency_matrix[trans("z"), trans("x")] = 7

	graph_1 = Graph(5)
	graph_1.adjacency_matrix[trans("s"), trans("t")] = 6
	graph_1.adjacency_matrix[trans("s"), trans("y")] = 7

	graph_1.adjacency_matrix[trans("t"), trans("x")] = -5
	graph_1.adjacency_matrix[trans("t"), trans("y")] = -8
	graph_1.adjacency_matrix[trans("t"), trans("z")] = -4

	graph_1.adjacency_matrix[trans("x"), trans("t")] = -2

	graph_1.adjacency_matrix[trans("y"), trans("x")] = -3
	graph_1.adjacency_matrix[trans("y"), trans("z")] = -9

	graph_1.adjacency_matrix[trans("z"), trans("s")] = 2
	graph_1.adjacency_matrix[trans("z"), trans("x")] = -7


	print(find_negative_weight_cycle(graph_0))
	print()
	print(find_negative_weight_cycle(graph_1))