# Napišite program koji će izračunati na koliko se načina može proći N stepenica ako
# se možemo penjati po jednu ili dvije stepenice odjednom. Na primjer, tri stepenice
# mogu se proći na tri načina: 1-1-1, 1-2 i 2-1.


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
    return len(remove_duplicate_combinations(recursion(coins_sum, coins)))


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
    print(f(4, (1, 2)))