# Riješite zadatak 5 tako da se ispisuju kombinacije kovanica. Na primjer:
# >>> iznos_kovanica (6, (1, 2, 5), [])
# [2, 2, 2]
# [1, 5]
# [1, 1, 2, 2]
# [1, 1, 1, 1, 2]
# [1, 1, 1, 1, 1, 1]


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


def f(coins_sum, coins):
    return remove_duplicate_combinations(recursion(coins_sum, coins))


def recursion(coins_sum, coins):
    if coins_sum < 0:
        return []
    if coins_sum == 0:
        return [[]]
    combinations = []
    for previous_coin in coins:
        combos = recursion(coins_sum - previous_coin, coins)
        for combo in combos:
            combo.append(previous_coin)
            combinations.append(combo)
    return combinations


if __name__ == '__main__':
    for x in f(6, (1, 2, 5)):
        print(x)
