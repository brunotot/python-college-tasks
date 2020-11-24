# Napišite funkciju koja će iz mape (dictionary) ukloniti sve duplikate. Primjerice,
# ako mapa sadrži {'a': 84, 'b': 11, 'c': 84} onda ta funkcija treba vratiti mapu
# {'a': 84, 'b': 11}.


def remove_duplicates(map_value):
    new_map = {}
    for key in map_value:
        if map_value[key] not in new_map.values():
            new_map[key] = map_value[key]
    return new_map

if __name__ == "__main__":
    map_value = {
        'a': 84,
        'b': 11,
        'c': 84
    }

    print(remove_duplicates(map_value))