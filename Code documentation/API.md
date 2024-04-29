Floyd_Warshall (graph) is the function

Graph is the input

Result gives back a 2D list with the distances on the shortest paths betweene each pair of vertices. The shortest path distance between vertex i and j is represented by the value at dist [i[][j]

Variable: V and distance

Dist [i][j] is the expression. 

Floyd's alg revolves around this by determining if passing through k shortens the trip from i to j. In which case the shorter distance is updated in dist [i][j]