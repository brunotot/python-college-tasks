# Za dvodimenzionalni niz kao što je onaj ispod napišite program koji će dati par točaka
# koje su na najmanjoj udaljenosti jedna od druge. U primjeru ispod to su dvije točke
# na koordinatama (6, 4) i (7, 6), gdje je koordinata par (<redak>, <stupac>).


def get_closest_points(tocke):
    max_row = len(tocke)
    max_col = len(tocke[0])
    string_tocke = "".join(tocke)
    indices = [i for i in range(len(string_tocke)) if string_tocke[i] == '*']
    arr = list(map(lambda x: (int(x / max_col), x % max_col), indices))
    min_distance = max_col * max_row
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                distance = abs(arr[j][0] - arr[i][0]) + abs(arr[j][1] - arr[i][1])
                if distance < min_distance:
                    min_distance = distance
                    left = arr[j]
                    right = arr[i]
    return left, right


if __name__ == "__main__":
    tocke = [
        '....................',
        '....................',
        '.....*..............',
        '....................',
        '..............*.....',
        '....................',
        '....*.......*.......',
        '......*.............',
        '....................',
        '..........*.......*.',
    ]
    print(get_closest_points(tocke))
