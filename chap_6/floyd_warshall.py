import sys
sys.path.insert(0, '../chap_5')

from dag_shortest_paths import Graph

def floyd_warshall(graph):
	v_num = graph.v_num
	shortest = { (i, k, m):
		float("inf") for i in range(v_num)
			 		 for k in range(v_num)
			 		 for m in range(-1, v_num) }
	for i in range(v_num):
		shortest[i, i, v_num-1] = 0

	pred = { (i, k, m):
		None for i in range(v_num)
			 for k in range(v_num)
			 for m in range(-1, v_num) }

	for i in range(v_num):
		for k in range(v_num):
			shortest[i, k, -1] = graph.adjacency_matrix[i, k]
			pred[i, k, -1]     = i

	for x in range(v_num):
		for i in range(v_num):
			for k in range(v_num):
				if i is k: continue
				if shortest[i, k, x-1] > shortest[i, x, x-1] + shortest[x, k, x-1]:
					shortest[i, k, x] = shortest[i, x, x-1] + shortest[x, k, x-1]
					pred[i, k, x]     = pred[x, k, x-1]
				else:
					shortest[i, k, x] = shortest[i, k, x-1]
					pred[i, k, x]     = pred[i, k, x-1]

	return shortest, pred

if __name__ == '__main__':
	graph = Graph(4)
	graph.adjacency_matrix[0, 1] = 3
	graph.adjacency_matrix[0, 2] = 8

	graph.adjacency_matrix[1, 3] = 1

	graph.adjacency_matrix[2, 1] = 4

	graph.adjacency_matrix[3, 0] = 2
	graph.adjacency_matrix[3, 2] = -5

	shortest, pred = floyd_warshall(graph)
	v_num = graph.v_num
	print("shortest:")
	for i in range(v_num):
		for m in range(v_num):
			print(shortest[i, m, v_num-1], end=" ")
		print()
	print()

	print("pred:")
	for i in range(v_num):
		for m in range(v_num):
			print(pred[i, m, v_num-1], end=" ")
		print()