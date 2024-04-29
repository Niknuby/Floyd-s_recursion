import sys
import time
import random

NO_PATH = sys.maxsize

def floyd_warshall_recursive(graph, i, j, k):
    if k == -1:
        return graph[i][j]
    without_k = floyd_warshall_recursive(graph, i, j, k-1)
    with_k = floyd_warshall_recursive(graph, i, k, k-1) + floyd_warshall_recursive(graph, k, j, k-1)
    return min(without_k, with_k)

def floyd_warshall(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            graph[i][j] = floyd_warshall_recursive(graph, i, j, n-1)
    return graph

def performance_test():
    # Generate a random graph
    n = 10  # number of nodes
    graph = [[random.randint(1, 10) if i != j else 0 for j in range(n)] for i in range(n)]

    start_time = time.time()
    floyd_warshall(graph)
    end_time = time.time()

    print(f"Execution time of floyd_warshall: {end_time - start_time} seconds")

performance_test()
