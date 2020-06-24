from functools import reduce


def soma(inicial, atual):
    return inicial+atual


lista = [1, 3, 5, 10, 20]

soma = reduce(soma, lista)
print(soma)
