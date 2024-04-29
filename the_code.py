import sys

NO_PATH = sys.maxsize
def floyd_warshall_recursive(graph, i, j, k):
    """ This is an example of a function level docstring """ 
    if k == -1:
        return graph[i][j]
    without_k = floyd_warshall_recursive(graph, i, j, k-1)
    with_k = floyd_warshall_recursive(graph, i, k, k-1) + floyd_warshall_recursive(graph, k, j, k-1)
    return min(without_k, with_k)

def floyd_warshall(graph):
    """ This is an example of a function level docstring """
    n = len(graph)
    for i in range(n):
        for j in range(n):
            graph[i][j] = floyd_warshall_recursive(graph, i, j, n-1)
    return graph

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]

shortest_path_graph = floyd_warshall(graph)

for row in shortest_path_graph:
    print(row)