# Napišite svoju implementaciju Pythonove funkcije groupby.


def groupby(data, key=None):
    sorted_data = sorted(data, key=key)
    map_values = {}
    for elem in sorted_data:
        unique_key = elem if key is None else key(elem)
        if unique_key not in map_values.keys():
            map_values[unique_key] = [elem]
        else:
            map_values[unique_key].append(elem)
    return [(k, v) for k, v in map_values.items()]


if __name__ == '__main__':
    data = [
        (4, "B"),
        (1, "A"),
        (2, "C"),
        (3, "B")
    ]
    for key, group in groupby(data, key=lambda x: x[1]):
        print('key =', key, ", group =", list(group))







