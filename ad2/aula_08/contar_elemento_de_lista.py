from typing import Sequence


def contar(elemento, lista: Sequence) -> int:
    contador = 0
    for elemento_da_lista in lista:
        if elemento == elemento_da_lista:
            contador += 1

    return contador


print(contar('a', 'aaaba'))  # 4
print(contar('b', 'aaaba'))  # 1
print(contar('c', 'aaaba'))  # 0
