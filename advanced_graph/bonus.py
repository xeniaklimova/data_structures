#student 414

class Graph:

    def __init__(self) :
        self.nodes = []
        self.edges = []

    def add_node(self, node_id, weight) :
        self.nodes.append(node_id)

    def add_edge(self, source_id, end_id, weight) :
        self.edges.append([source_id, end_id, weight])


def build_Graph(nodes, edges) :

    G = Graph()

    for n in nodes :

        aux = n.split(', ')
        aux = [int(aux[0]), int(aux[1])]
        G.add_node(aux[0], aux[1])

    for e in edges :

        aux = e.split(', ')
        aux = [int(aux[0]), int(aux[1]), int(aux[2])]
        G.add_edge(aux[0], aux[1], aux[2])

    return G

def find(parent, element):
    if parent[element] != element:
        parent[element] = find(parent, parent[element])
    return parent[element]

def union(parent, score, node1, node2):
    if score[node1] < score[node2]:
        parent[node1] = node2
    elif score[node1] > score[node2]:
        parent[node2] = node1
    else:
        parent[node2] = node1
        score[node1] = score[node1] + 1


def print_output(final_tree) :
    string = ""
    for start, end, weight in final_tree:
        string = string + str(start) + ", " + str(end) + ", " + str(weight) + "; "

    print(string[:-2])


def minimum_spanning_forest(G) :

    final_tree = []
    i = 0
    j = 0

    G.edges.sort(key= lambda element: element[2])

    parent = []
    score = []

    for v in range(len(G.nodes)):
        parent.append(v)
        score.append(0)

    while j < len(G.nodes) - 1 and i <= len(G.edges)-1 :

        start, end, weight = G.edges[i]
        i = i + 1
        edge1 = find(parent, start)
        edge2 = find(parent, end)

        if edge1 != edge2:
            j = j + 1
            final_tree.append([start, end, weight])
            union(parent, score, edge1, edge2)


    print_output(final_tree)


if __name__ == '__main__':


    nodes = input().split('; ')
    edges = input().split('; ')

    G = build_Graph(nodes, edges)

    minimum_spanning_forest(G)


