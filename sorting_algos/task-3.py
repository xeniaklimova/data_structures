#!/usr/bin/env python3
# student 414

class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time
        self.total_time: int = selection_time + shipping_time


def partition(arr, left, right):
    pivot = arr[right].total_time
    i = left - 1

    for j in range(left, right):
        if arr[j].total_time <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[right]) = (arr[right], arr[i + 1])
    return i + 1


def sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        sort(arr, left, pivot - 1)
        sort(arr, pivot + 1, right)
    return arr


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

    length = len(timeAndIdList)-1

    result = sort(timeAndIdList, 0, len(timeAndIdList)-1)

    for order in result:
        print(str(order.id), end=" ")
    print("\n")

