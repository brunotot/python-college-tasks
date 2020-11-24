# Napišite program koji će za novčanu vrijednost od N eura pronaći najmanji broj
# novčanica ako su na raspolaganju novčanice od 200, 100, 50, 10, 5 i 1 euro. Na
# primjer, 27 eura bi se sastojalo od sljedećih novčanica: 2x10 + 1x5 + 2x1.


def f(n, available_banknotes):
    available_banknotes = sorted(set(available_banknotes), key=None, reverse=True)
    banknote_order = {}
    for banknote in available_banknotes:
        while n > banknote:
            if banknote in banknote_order:
                banknote_order[banknote] += 1
            else:
                banknote_order[banknote] = 1
            n -= banknote
    return banknote_order


if __name__ == "__main__":
    res = f(27, (200, 100, 50, 10, 5, 1))
    for key in res:
        print(res[key], "x", key)