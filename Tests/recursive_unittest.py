import sys
import unittest

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

class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        result = floyd_warshall(graph)
        expected_result = [[0, 7, 12, 8],
                           [NO_PATH, 0, 5, 7],
                           [NO_PATH, NO_PATH, 0, 2],
                           [NO_PATH, NO_PATH, NO_PATH, 0]]
        self.assertEqual(result, expected_result)
if __name__ == "__main__":
    unittest.main()  