# student 414

def find_duplicate(arr, n):

    sum = 0
    key = 0
    for x in arr:
        sum = sum + x

    key = int(sum - ((n - 1)*(n/2)))
    return key


if __name__ == "__main__":

    input = input()
    input = input.split(";")
    ids = []
    for d in input:
        id, value = d.split(',', 1)
        ids.append(int(id))

    n = len(ids)
    print(find_duplicate(ids, n))


