from core.dijkstra import *

G = Graph()
G.add_vertex('a')
G.add_vertex('b')
G.add_vertex('c')
G.add_vertex('d')
G.add_vertex('e')
 
G.add_edge('a', 'b', 2)
G.add_edge('a', 'c', 8)
G.add_edge('a', 'd', 5)
G.add_edge('b', 'c', 1)
G.add_edge('c', 'e', 3)
G.add_edge('d', 'e', 4)
 
#print(G) 
 
print(dijkstra(G, 'a'))
#print(shortest_path(G, 'b', 'e'))