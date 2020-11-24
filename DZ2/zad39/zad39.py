# Upotrebom funkcije reduce napišite izraz kojim se binarni broj prevodi u decimalni
# koristeći funkciju f(a, b) = 2a + b, gdje su a i b dvije susjedne binarne znamenke.


import functools


if __name__ == "__main__":
    print(functools.reduce(lambda a, b: 2 * a + int(b), "1000101", 0))