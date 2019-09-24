from random import randint


# Subprogramas
def preencher(lista_elems, qtd, min, max):
    for item in range(qtd):
        lista_elems.append(randint(min, max))


if __name__ == '__main__':
    # Programa Principal
    qtd_numeros = int(input('A Lista deve ter quantos valores?: '))
    minimo = int(input('Menor valor da faixa: '))
    maximo = int(input('Maior valor da faixa: '))
    numeros = []
    preencher(numeros, qtd_numeros, minimo, maximo)
    print(numeros)
