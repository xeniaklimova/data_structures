#!/usr/bin/env python3
# student 414

class Job:
    def __init__(self, id: int, p: int, w: int):
        self.id: int = id
        self.p:  int = p
        self.w:  int = w

        self.ratio: float = p/w


def merge(left, right):

    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if right[j].ratio < left[i].ratio:
            sorted_array.append(right[j])
            j += 1
        else:
            sorted_array.append(left[i])
            i += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


def sort(array):
    length = len(array)

    if length == 1:
        return array

    half = length // 2
    left = sort(array[:half])
    right = sort(array[half:])
    return merge(left, right)

    #raise NotImplementedError


if __name__ == '__main__':
    '''
    Retrieves and splits the input
    '''
    data = input()
    data = data.split('; ')
    jobList = []

    for d in data:
        id, p, w = d.split(', ', 2)
        job: Job = Job(int(id), int(p), int(w))
        jobList.append(job)

    
    '''
    TODO: Call your sorting function
    '''
    result = sort(jobList)

    for job in result:
        print(str(job.id), end=" ")
    print("\n")