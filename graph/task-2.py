from typing import List

ids = []
mydict = {}
final_list = []

def stringify_path(path: List):
    '''
    Build string to print
    '''
    ret = ''
    for id in path[:-1]:
        ret = f'{ret}{id}->'
    try:
        ret = f'{ret}{path[-1]}'
    except IndexError:
        pass

    return ret

def output(paths: List[List]):
    '''
    Prints all paths from the list in param
    '''
    paths_string = []
    for p in paths:
        paths_string.append(stringify_path(p))
    print(*paths_string, sep='\n')

'''
DO NOT CHANGE ABOVE
'''

def not_visited(node, path) ->  int:
    length = len(path)
    for i in range(length):
        if (path[i] == node):
            return 0
    return 1

def find_paths(mydict, start, finish) -> List[List]:
    store_paths = []
    current = []
    current.append(start)
    store_paths.append(current.copy())

    while store_paths:
        current = store_paths.pop(0)

        last_num = current[len(current)-1]

        if last_num == finish:
            final_list.append(current)

        if last_num in mydict:
            for neigh in mydict[last_num]:
                if not_visited(neigh, current) and neigh != 0:
                    new_current = current.copy()
                    new_current.append(neigh)
                    store_paths.append(new_current)

    final_list.sort()
    return final_list


if __name__ == '__main__':

    start, target = [int(x) for x in input().split('->')]
    data = input()
    data = data.split('; ')

    for d in data:
        id, followers = d.split(', ', 1)
        following_l: List = followers.split(', ')

        for f in following_l:
            if f != '':
                mydict[int(id)] = list(map(int, following_l))
                continue
            else:
                mydict[int(id)] = list(map(int, str(0)))

    paths: List[List] = find_paths(mydict, start, target)
    output(paths)
