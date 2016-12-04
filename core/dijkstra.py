# python 3 only!!!
import collections
import math


class Graph:
    '''graph class inspired by https://gist.github.com/econchick/4666413'''
    def __init__(self):
        self.vertices = set()

        # makes the default value for all vertices an empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex:
            pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    # initializations
    S = set()
    delta = dict.fromkeys(list(graph.vertices), math.inf)
    previous = dict.fromkeys(list(graph.vertices), None)

    # then we set the path length of the start vertex to 0
    delta[start] = 0

    # while there exists a vertex v not in S
    while S != graph.vertices:
        v = min((set(delta.keys()) - S), key=delta.get)
        # for each neighbor of v not in S
        for neighbor in set(graph.edges[v]) - S:
            new_path = delta[v] + graph.weights[v, neighbor]
            if new_path < delta[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                delta[neighbor] = new_path
                #print(delta[neighbor])
                previous[neighbor] = v
        S.add(v)
    return (delta, previous)


def shortest_path(graph, start, end):
    delta, previous = dijkstra(graph, start)
    path = []
    vertex = end
    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]
    path.reverse()
    return path
