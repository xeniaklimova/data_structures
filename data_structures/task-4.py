# student 414

import sys
class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = ('1.1.1977', sys.maxsize)
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):  # parent node is Heap[(i - 1)/ 2]
        return pos // 2


    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):  # left child is Heap[(2 * i) + 1]
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos

    def rightChild(self, pos):  # right child is Heap[(2 * i) + 2]
        return 2 * pos + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):  # not (i >= (self.cursize // 2)), meaning if cur is larger than its parent

        if self.size//2 <= pos <= self.size:
            return True
        else:
            return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if self.Heap[pos][1] < self.Heap[self.leftChild(pos)][1] or self.Heap[pos][1] < self.Heap[self.rightChild(pos)][1]:
                if self.Heap[self.rightChild(pos)][1] < self.Heap[self.leftChild(pos)][1]:
                    self.swap(pos, self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):  # This is the heappush
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        level = self.size
        while self.Heap[level][1] > self.Heap[self.parent(level)][1]:
            self.swap(level, self.parent(level))
            level = self.parent(level)

    # Function to print the contents of the heap
    def Print(self):

        for i in range(1, (self.size // 2) + 1):
            print(i)
            print("PARENT : " + str(self.Heap[i]) +
                  "LEFT CHILD : " + str(self.Heap[2 * i]) +
                  "RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):  # return the root element
        value = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return value


# Driver Code 2022−09−08, 23, 371; 2022−09−08, 2, 311; 2022−09−08, 12, 43; 2021−03−21, 4, 129; 2021−03−21, 4, 100
if __name__ == "__main__":
    input = input()
    input = input.split(";")
    dates = []
    values = []
    for d in input:
        date = d.split(',', 2)  # turned to this: date: ['2022−09−08', ' 23', ' 371']

        dates.append(date[0].lstrip())
        values.append(date[2])

    values = [int(x) for x in values]

    tuples = list(zip(dates, values))  # [('2022−09−08', 371), (' 2022−09−08', 3171), (' 2022−09−08', 43)]


    heap = MaxHeap(len(tuples) + 1)
    for t in tuples:
        heap.insert(t)

    result = heap.extractMax()
    print(str(result[0]) + "," + str(result[1]))




