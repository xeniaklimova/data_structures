# student 414
import sys

INF = sys.maxsize

list = []

class Graph:

    def __init__(self) :
        self.edges = []
        self.nodes = []

    def add_node(self, node_id, weight):
        self.nodes.append(node_id)

    def add_edge(self, source_id, end_id, weight) : 
        self.edges.append([source_id, end_id, weight])

def path(start, end, next):
    if next[start][end] == 0:
        return[]
    path = [start]
    while start != end:
        start = next[start][end]
        path.append(start)
    return path


def floyd_warshall(graph):
    dist = [[INF for i in range(graph_len)] for j in range(graph_len)]

    next = [[0 for i in range(graph_len)] for j in range(graph_len)]

    for start, end, weight in G.edges:
        dist[start][end] = weight
        next[start][end] = end

    for node in G.nodes:
        dist[node][node] = 0
        next[node][node] = node

    for k in range(1, graph_len):
        for i in range(1, graph_len):
            if dist[i][k] != INF:
                for j in range(1, graph_len):
                    if dist[k][j] != INF:
                            temp = dist[i][k] + dist[k][j]
                            if dist[i][j] == INF or dist[i][j] > dist[i][k] + dist[k][j]:
                                dist[i][j] = temp
                                next[i][j] = next[i][k]


    for i in range(graph_len):
        for j in range(graph_len):
            item = path(i, j, next)
            if item:
                list.append(path(i, j, next))


    return list



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


if __name__ == '__main__':

    nodes = input().split('; ')
    edges = input().split('; ')
    G = build_Graph(nodes, edges)
    graph_len = len(edges)

    paths = floyd_warshall(G.edges)

    paths_len = len(paths)


    flattened = []

    for path in paths:
        for val in path:
            flattened.append(val)

    counter = 0
    mydict = {}

    for node in range(len(G.nodes)):
        for num in range(len(flattened)):
            if(G.nodes[node] == flattened[num]):
                counter += 1
        mydict[G.nodes[node]] = counter
        counter = 0


    final = max(mydict, key=mydict.get)

    print(str(final))

    # print(str(c))

