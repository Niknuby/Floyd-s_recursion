import sys
import timeit

def floyd_iterative(graph):
    """
    Perform Floyd's algorithm iteratively to find shortest paths between all pairs of vertices.
    
    Args:
        graph (list): The adjacency matrix representing the graph.
        
    Returns:
        list: The shortest distance matrix.
    """
    n = len(graph)

    # Initialize the distance matrix with the given graph
    dist = [row[:] for row in graph]

    # Iterate over intermediate nodes
    for k in range(n):
        # Iterate over source nodes
        for i in range(n):
            # Iterate over destination nodes
            for j in range(n):
                # If there is a shorter path through k
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Define the graph
NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

# Define a function to measure performance
def measure_performance():
    floyd_iterative(graph)

# Measure the performance
execution_time = timeit.timeit(measure_performance, number=10)
print("Execution time:", execution_time, "seconds for 10 iterations")