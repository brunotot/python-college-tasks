# Koristeći samo funkciju reduce (iz modula functools) i bez upotrebe petlje ili rekurzije,
# napišite funkciju ukupno koja će za zadani niz mapa s parovima cijena/vrijednost dati
# zbroj svih vrijednosti, kako je ispod pokazano (funkcija reduce radi isto kao funkcija
# redukcija iz jednog od prethodnih zadataka).
# >>> podaci2 = [{'cijena': 25}, {'cijena': 10},
# {'cijena': 10}, {'cijena': 15}, {'cijena': 30}]
#
# >>> ukupno(podaci2)
# 90


import functools


def total(data):
    return functools.reduce(lambda a, b: a + b['cijena'], data, 0)


if __name__ == "__main__":
    print(total([{'cijena': 25}, {'cijena': 10}, {'cijena': 10}, {'cijena': 15}, {'cijena': 30}]))