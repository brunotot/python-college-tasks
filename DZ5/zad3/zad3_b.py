# Prefiksni oblik izraza ima oblik <operator> <operand-1> <operand-2>, s tim da
# <operand-N> može i sam biti izraz u prefiksnom obliku. Na primjer, a+b*c se u
# prefiksnom obliku zapisuje kao +a*bc. Definirajte funkciju vrijednost koja za zadani
# izraz u prefiksnom obliku zadanom kao Pythonova lista daje rezultat tog izraza. Na
# primjer, vrijednost izraza [mnozi, 2, 7] je 14 ako je funkcija mnozi definirana tako
# da pomnozi dvije vrijednosti. Slično, funkcija zbroji daje zbroj svojih parametara.

# b) Definirajte ove funkcije tako da rade s bilo kojim brojem parametara


from functools import reduce


def multiply(*numbers):
    return reduce((lambda x, y: x * y), numbers)


def add(*numbers):
    return reduce((lambda x, y: x + y), numbers)


def evaluate(operation, *expressions):
    expressions_evaluations = []
    for exp in expressions:
        expressions_evaluations.append(evaluate(exp[0], *exp[1:]) if isinstance(exp, list) else exp)
    return operation(*expressions_evaluations)


if __name__ == "__main__":
    print(evaluate(multiply, 2, 3, [add, 1, 2, 3, 4]))
