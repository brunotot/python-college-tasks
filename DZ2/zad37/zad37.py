# Napišite operaciju sortiranja tako da se redoslijed elemenata u rezultirajućem nizu
# može zadati kao parametar:
#
# >>> sortiraj ([1, 5, 2], lambda x, y: x > y)
# [5, 2, 1]
#
# >>> sortiraj ([1, 5, 2], lambda x, y: x < y)
# [1, 2, 5]
#
# >>> sortiraj ([4, "2", 8, "5"], lambda x, y: int(x) < int(y))
# ['2', 4, '5', 8]


def sort(l, key=None):
    for i in range (0, len(l)):
        for j in range (0, len(l) - i - 1):
            if key(l[j + 1], l[j]):
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


if __name__ == "__main__":
    print(sort([4, "2", 8, "5"], lambda x, y: int(x) < int(y)))