# student 414
import math

class Graph:

    def __init__(self) :
        self.nodes = {}
        self.edges = {}


    def add_node(self, node_id, weight) : 

        node = {node_id: weight}
        self.nodes.update(node)

    def add_edge(self, source_id, end_id, weight) : 

        tuples = end_id, weight
        self.edges.setdefault(source_id,[])
        self.edges[source_id].append(tuples)



def build_Graph(nodes, edges) :
    G = Graph()

    for n in nodes : 
        aux = n.split(', ')

        temp1 = int(aux[0])
        temp2 = int(aux[1])
        temp_node = (temp1, temp2)

        G.add_node(temp_node, weight=int(aux[2]))

    for e in edges : 
        aux = e.split(', ')

        temp1 = int(aux[0])
        temp2 = int(aux[1])
        temp = (temp1, temp2)

        auxn1 = int(aux[2])
        auxn2 = int(aux[3])
        auxn = (auxn1, auxn2)

        G.add_edge(temp, auxn, weight=int(aux[4]))    

    return G


def print_output(s_path) :
    final_res = ""
    for (x,y) in s_path:
        final_res = final_res + str(x) + ", "+ str(y) + "->"

    print(final_res[:-2])


def astar_shortest_path(G, source_id, end_id, heuristic):

    open = set({source_id})

    closed = set()
    graph = {}
    parents = {}

    graph[source_id] = 0
    parents[source_id] = source_id

    while len(open) > 0:
        n = None

        for v in open:
            if n == None or graph[v] + heuristic(source_id, n) < graph[n] + heuristic(source_id, v):
                n = v

        if n == end_id or G.edges[n] == None:
            pass

        else:
            for (m, weight) in G.edges[n]:

                if m not in open and m not in closed:
                    open.add(m)
                    parents[m] = n
                    graph[m] = graph[n] + weight

                else:
                    if graph[m] > graph[n] + weight:

                        graph[m] = graph[n] + weight

                        parents[m] = n

                        if m in closed:
                            closed.remove(m)
                            open.add(m)
        if n == None:
            return None

        if n == end_id:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(source_id)
            path.reverse()
            return path

        open.remove(n)
        closed.add(n)

    return None


def heuristic(a, b) :
    (x1, y1) = a
    (x2, y2) = b
    return math.sqrt(pow(x2-x1, 2) + pow(y2 - y1, 2))



if __name__ == '__main__':

    nodes = input().split('; ')
    edges = input().split('; ')

    G = build_Graph(nodes, edges)

    source_id =max(G.nodes, key=G.nodes.get)
    temp = G.nodes.copy()
    del temp[source_id]
    end_id = max(temp, key=temp.get)


    s_path = astar_shortest_path(G, source_id, end_id, heuristic)
    print_output(s_path)




