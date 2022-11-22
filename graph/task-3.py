from typing import List, Tuple
import itertools

#student 414

nodearr = {}
infinity = 1000000000
dist = {}
final = ""

def dijkstra(graph, start, end):
    unvisited = {n: float(infinity) for n in graph}
    unvisited[start] = 0

    visited = {}
    parents = {}

    while unvisited:
        min_node = min(unvisited, key=unvisited.get)

        for neigh in graph[min_node][1]:
            if neigh in visited:
                continue
            new_dist = unvisited[min_node] + graph[min_node][0]

            if new_dist < unvisited[neigh]:
                unvisited[neigh] = new_dist
                parents[neigh] = min_node
        visited[min_node] = unvisited[min_node]
        unvisited.pop(min_node)

        if min_node == end:
            break

    result = [end]
    while True:
        key = parents[result[0]]
        result.insert(0, key)
        if key == start:
            break

    return result

if __name__ == '__main__':

    start_id, end_id = [int(i) for i in input().split(' ')]

    data = input()
    data = data.split('; ')

    for counter, d in enumerate(data):

        id, num_likes, following = d.split(', ', 2)
        following_l = following.split(', ')

        for f in following_l:
            if f != '':
                nodearr[int(id)] = (1 / int(num_likes)), list(map(int, following_l))
            else:
                nodearr[int(id)] = (1 / int(num_likes)), list(map(int, str(0)))
                continue

    path = dijkstra(nodearr, start_id, end_id)

    for i in range(len(path)):
        final += str(path[i]) + " "
    final += "\n"
    print(final)









