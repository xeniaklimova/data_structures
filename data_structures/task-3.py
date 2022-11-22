# student 414

def add_value(dict_obj, key, value):

    if key not in dict_obj.keys():
        dict_obj.setdefault(key, [])
    dict_obj[key].append(value)


def get_max(dic, date):

    iterable = dic[date]

    curmax = iterable[0]
    for i in range(len(iterable)):
        if iterable[i][1] > curmax[1]:
            curmax = iterable[i]

    return curmax


if __name__ == "__main__":
    input = input()
    input = input.split(";")
    requested_date = input[0]
    input.pop(0)
    data = []

    for d in input:
        date, id, value = d.split(',', 2)

        instance = (date, (int(id), int(value)))
        data.append(instance)


    my_dict = {}

    for v in range(len(data)):
        add_value(my_dict, data[v][0].lstrip(), data[v][1])

    result = get_max(my_dict, requested_date)
    id = result[0]
    level = result[1]
    print(str(id) + "," + str(level))
