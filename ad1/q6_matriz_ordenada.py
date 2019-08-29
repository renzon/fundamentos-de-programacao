from random import randint
from typing import List


def produzir_matriz(n: int, m: int):
    matriz = [[randint(10, 100) for _ in range(m)] for _ in range(n)]
    return matriz


def imprimir_matriz(matriz: List[List[int]]) -> None:
    """Imprime Matriz"""
    for linha in matriz:
        print(*linha)



def ordernar_por_soma_de_linha(matriz: List[List[int]]) -> List[List[int]]:
    lista_soma_de_linhas = []
    for i, linha in enumerate(matriz):
        tpl = (sum(linha), i, linha)
        lista_soma_de_linhas.append(tpl)
    lista_ordenada=[]
    for _, _, linha in ordenar(lista_soma_de_linhas):
        lista_ordenada.append(linha)

    return lista_ordenada


def ordenar(lista):
    tamanho = len(lista)
    if tamanho <= 1:
        return lista
    meio = tamanho // 2
    pivo = lista[meio]
    menores_ou_iguais_ao_pivo = []
    maiores_que_o_pivo = []
    elementos_a_esquerda_do_pivo = lista[:meio]
    elementos_a_direita_do_pivo = lista[meio + 1:]
    for n in elementos_a_esquerda_do_pivo + elementos_a_direita_do_pivo:
        if n <= pivo:
            menores_ou_iguais_ao_pivo.append(n)
        else:
            maiores_que_o_pivo.append(n)
    return ordenar(menores_ou_iguais_ao_pivo) + [pivo] + ordenar(maiores_que_o_pivo)


n_m_str = input('Digite as dimensões de uma matriz bidimentisional: ')
n, m = n_m_str.split()
n = int(n)
m = int(m)

valores = produzir_matriz(n, m)
imprimir_matriz(valores)
print()
imprimir_matriz(ordernar_por_soma_de_linha(valores))
