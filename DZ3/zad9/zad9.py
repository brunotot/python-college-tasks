# Riješite zadatak 5 tako da se može zadati količina svake kovanice, s tim da se i dalje
# ispisuju kombinacije kao u zadatku 8. To treba riješiti tako da se kao treći parametar
# zada mapa kod koje je ključ oznaka kovanice, a vrijednost broj za količinu te kovanice.
# U sljedećem primjeru kovanica od 1 cent smije biti najviše dvije, a kovanica od 2 centa
# najviše jedna dok je broj ostalih kovanica neograničen:
# >>> iznos_kovanica (6, (1, 2, 5), {1: 2, 2: 1}, [])
# [1, 5]


def get_key_counter_map(combination):
    key_counter_map = {}
    for key in combination:
        if key in key_counter_map:
            key_counter_map[key] += 1
        else:
            key_counter_map[key] = 1
    return key_counter_map


def remove_duplicate_combinations(combinations):
    unique = []
    key_counter_map_list = []
    for combination in combinations:
        key_counter_map = get_key_counter_map(combination)
        if key_counter_map not in key_counter_map_list:
            unique.append(combination)
            key_counter_map_list.append(key_counter_map)
    return unique


def validate_combination_maps(rule_map, combination):
    validation_map = get_key_counter_map(combination)
    for rule_key in rule_map:
        if rule_key in validation_map and rule_map[rule_key] < validation_map[rule_key]:
            return False
    return True


def recursive(coins_sum, coins, limitations):
    if coins_sum < 0:
        return []
    if coins_sum == 0:
        return [[]]
    combinations = []
    for previous_coin in coins:
        combos = recursive(coins_sum - previous_coin, coins, limitations)
        for combo in combos:
            combo.append(previous_coin)
            combinations.append(combo)
    return combinations


def f(coins_sum, coins, limitations):
    return [
                combination for combination in remove_duplicate_combinations(recursive(coins_sum, coins, limitations))
                if validate_combination_maps(limitations, combination)
           ]


if __name__ == '__main__':
    for x in f(6, (1, 2, 5), {1: 2, 2: 1}):
        print(x)