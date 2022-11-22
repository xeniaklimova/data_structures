#!/usr/bin/env python3
# student 414

class Order:
    def __init__(self, id: int, selection_time: int, shipping_time: int):
        self.id: int = id
        self.selection_time: int = selection_time
        self.shipping_time:  int = shipping_time

        '''
        Remove me if you don't need me.
        Add a method to assign to me.
        '''
        self.next: Order = None

    '''
    Make your life easier and your code prettier, use `Operator Overloading`.
    '''


def sort(list):
    '''
    TODO: Implement your sorting function and add the parameters you need.
    '''

    for d in range(len(list)):
        min_index = d
        for j in range(d+1, len(list)):
            if list[min_index][1] > list[j][1]:
                min_index = j

        list[d], list[min_index] = list[min_index], list[d]


if __name__ == '__main__':
    '''
    Retrieves and splits the input
    '''
    data = input()
    data = data.split('; ')
    listOfTimes = dict()
    finalString = ""

    for d in data:
        id, selection_t, shipping_t = d.split(', ', 2)
        order: Order = Order(int(id), int(selection_t), int(shipping_t))
        '''
        TODO: Append the `order` object to your structure.
        1, 500, 100; 2, 700, 100; 3, 100, 100
        '''
        listOfTimes.update({id: int(selection_t) + int(shipping_t)})

    '''
    TODO: Call your sorting function
    '''
    itemlist = list(listOfTimes.items())

    sort(itemlist)

    '''
    TODO: Print in stdout the id's of the sorted list (order.id) in one line separated by spaces.
    Terminate with a new line.
            i.e: 1 2 3 4 5 6\n
    '''
    for i in range(len(itemlist)):
        finalString += str(itemlist[i][0]) + " "
    finalString += "\n"
    print(finalString)



