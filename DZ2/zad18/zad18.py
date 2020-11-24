# Napišite funkciju sastavljena(a, b) koja daje True ako se lista a može sastaviti od
# skupine lista u b. U prvom primjeru ispod, lista [5, 1, 7, 4, 4, 9, 2, 1] može se sastaviti
# od lista [5] + [1] + [7, 4, 4] + [9, 2, 1], tako da funkcija daje True. U drugom primjeru
# ne možemo dobiti listu a jer poredak elemenata u listi [9, 1, 2] ne odgovara onome u
# listi a. U trećem primjeru također ne možemo sastaviti zadanu listu.


def composition(a, b):
    string_a = "".join(str(x) for x in a)
    for elem in b:
        string_b = "".join(str(x) for x in elem)
        string_a = string_a.replace(string_b, "")
    return len(string_a) == 0


if __name__ == "__main__":
    a = [5, 1, 7, 4, 4, 9, 2, 1]
    b = [[9, 2, 1], [1], [7, 4, 4], [5]]
    print(composition(a, b))
