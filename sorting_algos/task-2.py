#!/usr/bin/env python3
# student 414


class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time
        self.total_time: int = selection_time + shipping_time


def merge(left, right):

    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if right[j].total_time < left[i].total_time:
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

    half = length//2
    left = sort(array[:half])
    right = sort(array[half:])
    return merge(left, right)


#     # raise NotImplementedError




if __name__ == '__main__':
    '''
    Retrieves and splits the input
    1, 500, 100; 2, 700, 100; 3, 100, 100
    '''
    data = input()
    data = data.split('; ')
    timeAndIdList = []

    for d in data:
        id, selection_t, shipping_t = d.split(', ', 2)
        order: Order = Order(int(id), int(selection_t), int(shipping_t))
        timeAndIdList.append(order)

    '''
    TODO: Call your sorting function
    '''
    result = sort(timeAndIdList)

    for order in result:
        print(str(order.id), end=" ")
    print("\n")


