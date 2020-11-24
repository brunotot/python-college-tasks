# Neka je zadan broj N i dvije operacije:
#   (a) dodaj 1 (x+1)
#   (b) udvostruči (x*2)
# gdje je x rezultat prethodne operacije. Napišite program koji će pronaći minimalni
# broj operacija da bi se došlo do broja N počevši od 0. Neka je, na primjer, N = 7. Tada
# je minimalni broj operacija 0+1=1, 1+1=2, 1+2=3, 3*2=6, 6+1=7, što je ukupno pet
# operacija. Međutim, sljedeći niz operacija nije minimalan: 0+1=1, 1+1=2, 2*2=4,
# 4+1=5, 5+1=6, 6+1=7, što daje ukupno šest operacija. Ovdje je problem u tome što
# nakon množenja 2*2=4 moramo imati još tri zbrajanja.

import sys


def minimum(n):
    min_combinations = [sys.maxsize] * (n + 1)
    min_combinations[1] = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            # // --> floor operator, npr. 8 // 3 = 2
            x = min_combinations[i // 2]
            if x + 1 < min_combinations[i]:
                min_combinations[i] = x + 1
        x = min_combinations[i - 1]
        if x + 1 < min_combinations[i]:
            min_combinations[i] = x + 1
    return min_combinations[n] + 1


if __name__ == "__main__":
    print(minimum(6))
    # 0+1
    # 1+1
    # 2+1
    # 3*2
