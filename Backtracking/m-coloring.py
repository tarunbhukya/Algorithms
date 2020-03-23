"""
Given an undirected graph and a number m,
determine if the graph can be colored with at most m colors such that no two adjacent vertices
of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices.
"""


def is_safe(graph, test_color, color_vertices, vertice_index):
    for v in range(len(color_vertices)):
        if graph[vertice_index][v] == 1 and test_color == color_vertices[v]:
            return False
    return True


def solve_util(graph, colors_size, color_vertices, vertice_index):
    if vertice_index == len(graph):
        return True

    for i in range(colors_size):
        if is_safe(graph, i+1, color_vertices, vertice_index):
            color_vertices[vertice_index] = i + 1
            if solve_util(graph, colors_size, color_vertices, vertice_index + 1):
                return True
            color_vertices[vertice_index] = 0
    return False



def solve_graph(graph, colors_size):
    color_vertices = [0 for i in range(len(graph))]
    if solve_util(graph, colors_size, color_vertices, 0):
        print("vertices colors are :")
        print(color_vertices)
    else:
        print("No Solution")


input = [[0,1,1,1],
         [1,0,1,0],
         [1,1,0,1],
         [1,0,1,0]]
colors_size = 3

solve_graph(input, colors_size)
