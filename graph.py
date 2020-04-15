class Vertices():
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight):
        self.edges[vertex] = weight

class Graph():
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertices(self, vertices):
        self.graph_dict[vertices.value] = vertices

    def add_edge(self, from_vertices, to_vertices, weight=0):
        self.graph_dict[from_vertices.value].add_edge(to_vertices.value, weight)
        if not self.directed:
            self.graph_dict[to_vertices.value].add_edge(from_vertices.value, weight)

    def find_path(self, from_vertices, to_vertices):
        start = [from_vertices]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop()
            seen[current_vertex] = True
            if current_vertex == to_vertices:
                return True
            edges = set(self.graph_dict[current_vertex].get_edges())
            vertices_to_vist = [edge for edge in edges if edge not in seen]
            start += vertices_to_vist
        return False

#test cases
# one = Vertices(1)
# two = Vertices(2)
# three = Vertices(3)
# four = Vertices(4)
# graph = Graph()
# graph.add_vertices(one)
# graph.add_vertices(two)
# graph.add_vertices(three)
# graph.add_vertices(four)
# graph.add_edge(one, two)
# graph.add_edge(two, three)
# graph.add_edge(three, four)
# print(graph.find_path(2, 5))
<<<<<<< HEAD
=======


>>>>>>> 9194ef0523e1110b6086012b8f7221b6e5aac693
