# student 414

def find_max_ind(arr):

    # TODO: write program that returns the index of the maximum.
    currmax = arr[0]
    for i in range(len(arr)):
        if currmax < arr[i]:
            currmax = arr[i]
            index = i

    return index


if __name__ == "__main__":

    str_array = input()
    arr_str = str_array.rstrip()
    arr = list(map(int, arr_str.split(' ')))

    print(find_max_ind(arr))
