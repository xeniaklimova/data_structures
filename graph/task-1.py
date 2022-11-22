from typing import List

stack = []
mydict = {}
ids = []
visited = set()

def output():
    for id in stack[:-1]:
        print(f'{id}->', end='')
    try:
        print(f'{stack[-1]}')
    except IndexError:
        pass


def dfs(visited, start, target, stack):

    stack.append(start)
    if start == target:
        output()
        return

    visited.add(start)

    for neigh in mydict[start]:
        if neigh not in visited and neigh != 0:
            dfs(visited, neigh, target, stack)

    del stack[-1]


if __name__ == '__main__':

    start, target = [int(x) for x in input().split('->')]
    data = input()
    data_l: List = data.split('; ')
    numNodes = len(data_l)

    for d in data_l:
        id, followers = d.split(', ', 1)

        following_l: List = followers.split(', ')
        ids.append(int(id))

        for f in following_l:
            if f != '':
                mydict[int(id)] = list(map(int, following_l))
                continue
            else:
                mydict[int(id)] = list(map(int, str(0)))

    dfs(visited, start, target, stack)
