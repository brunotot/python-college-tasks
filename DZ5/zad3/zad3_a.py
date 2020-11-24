# Prefiksni oblik izraza ima oblik <operator> <operand-1> <operand-2>, s tim da
# <operand-N> može i sam biti izraz u prefiksnom obliku. Na primjer, a+b*c se u
# prefiksnom obliku zapisuje kao +a*bc. Definirajte funkciju vrijednost koja za zadani
# izraz u prefiksnom obliku zadanom kao Pythonova lista daje rezultat tog izraza. Na
# primjer, vrijednost izraza [mnozi, 2, 7] je 14 ako je funkcija mnozi definirana tako
# da pomnozi dvije vrijednosti. Slično, funkcija zbroji daje zbroj svojih parametara.

# a) Definirajte funkcije mnozi i zbroji tako da rade s točno 2 parametra.
# >>> x = [mnozi , 2, [mnozi, [zbroji , [zbroji, 2, 1], 7], [mnozi, 4, 2]]]
# >>> vrijednost (x)
# >>> 160


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


def evaluate(operation, exp1, exp2):
    return operation(
        evaluate(exp1[0], exp1[1], exp1[2]) if isinstance(exp1, list) else exp1,
        evaluate(exp2[0], exp2[1], exp2[2]) if isinstance(exp2, list) else exp2
    )


if __name__ == "__main__":
    print(evaluate(multiply, 2, [multiply, [add, [add, 2, 1], 7], [multiply, 4, 2]]))

