# Napišite funkciju spoji_mape(a, b) koja će ”spojiti” dvije mape, a i b, na sljedeći
# način:
# (a)
# Ako za isti ključ vrijednost niti u jednoj od mapa nije tipa list onda za vrijednost
# x iz mape a i vrijednost y iz mape b u novoj mapi vrijednost treba biti lista [x, y].

# (b)
# Ako za isti ključ jedna mapa sadrži listu [e1, e2, ..., en], a druga vrijednost x
# nekog drugog tipa, onda nova mapa za taj ključ treba sadržavati [e1, e2, ..., en, x].

# (c) Ako obje mape za dotični ključ sadrže liste onda nova mapa za taj ključ treba
# sadržavati listu s vrijednostima iz obje liste.


def merge_a(elem_a, elem_b):
    return [elem_a, elem_b]


def merge_b(elem_a, elem_b):
    list = elem_a
    appender_elem = elem_b
    if type(elem_b) is list:
        list = elem_b
        appender_elem = elem_a
    list.append(appender_elem)
    return list


def merge_c(list_a, list_b):
    list = list_a
    for elem in list_b:
        list.append(elem)
    return list


def spoji_mape(a, b):
    result_map = {}
    for key in a:
        for key_b in b:
            if key == key_b:
                if type(a[key]) is not list and type(b[key]) is not list:
                    result_map[key] = merge_a(a[key], b[key])
                elif (type(a[key]) is list and type(b[key]) is not list) or (type(b[key]) is list and type(a[key]) is not list):
                    result_map[key] = merge_b(a[key], b[key])
                else:
                    result_map[key] = merge_c(a[key], b[key])
                break

    return result_map


if __name__ == '__main__':
    map1 = {}
    map2 = {}

    map1["a"] = [1, 2]
    map2["a"] = 3

    map1["b"] = [4, 5]
    map2["b"] = [6, 7]

    map1["c"] = 8
    map2["c"] = 9

    map1["d"] = -1

    result_map = spoji_mape(map1, map2)
    print(result_map)
