n_m_str = input('Digite as dimensões de uma matriz bidimentisionsl: ')
n, m = n_m_str.split()
n = int(n)
m = int(m)
from random import randint
from typing import List


def produzir_matriz(n: int, m: int):
    matriz = [[randint(100, 1000) for _ in range(m)] for _ in range(n)]
    return matriz


def imprimir_matriz(matriz: List[List[int]]) -> None:
    """Imprime Matriz"""
    for linha in matriz:
        print(*linha)


def calcular_item_maximo(matriz):
    posicao = (0, 0)
    valor_max = 0
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor_max < valor:
                valor_max = valor
                posicao = (i, j)
    print(f'Posição do Maior: {posicao} Maior Valor: {valor_max}')


def calcular_soma_das_colunas(matriz):
    for i, coluna in enumerate(zip(*matriz)):
        print(f'Soma da Coluna {i} = {sum(coluna)}')


def calcular_soma_das_linhas(matriz):
    for i, linha in enumerate(matriz):
        print(f'Soma da Linha {i} = {sum(linha)}')


matriz = produzir_matriz(n, m)
print()
imprimir_matriz(matriz)
print()
calcular_item_maximo(matriz)
print()
calcular_soma_das_linhas(matriz)
print()
calcular_soma_das_colunas(matriz)
