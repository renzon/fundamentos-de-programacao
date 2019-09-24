# Subprogramas
from ad2.aula_08.lista_aleatoria import preencher


def remover_duplicatas(elems):
    indice = 0
    while indice < len(elems):
        if elems.count(elems[indice]) == 1:
            indice += 1
        else:
            elems.remove(elems[indice])
    return None


# Programa Principal
numeros = []
preencher(numeros, 100, 0, 40)
print(numeros)
remover_duplicatas(numeros)
print(numeros)
