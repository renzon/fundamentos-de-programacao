# nome_do_arquivo = input('Digite o nome do entrada de entrada: ')
from math import inf

nome_do_arquivo = 'entrada.txt'
centroide = (0, 0)
with open(nome_do_arquivo, 'r', encoding='utf8') as arquivo:
    soma_x = 0
    soma_y = 0
    contador = 0
    for linha in arquivo:
        linha = linha.strip()
        x, y = linha.split()
        x = float(x)
        y = float(y)
        soma_x += x
        soma_y += y
        contador += 1
    centroide = (soma_x / contador, soma_y / contador)
    print(f'Centroide: ({centroide[0]:.1f}, {centroide[1]:.1f})')

with open(nome_do_arquivo, 'r', encoding='utf8') as arquivo:
    menor_distancia = inf
    x_centroide, y_centroide = centroide
    ponto_mais_proximo = centroide
    for linha in arquivo:
        linha = linha.strip()
        x, y = linha.split()
        x = float(x)
        y = float(y)
        distancia_ponto_atual = (x - x_centroide) ** 2 + (y - y_centroide) ** 2
        if distancia_ponto_atual < menor_distancia:
            menor_distancia = distancia_ponto_atual
            ponto_mais_proximo = (x, y)

    print(f'Ponto Mais Próximo: ({ponto_mais_proximo[0]:.1f}, {ponto_mais_proximo[1]:.1f})')

# print(eh_primo('ama'))
# print(eh_primo('socorrammesubinoonibusemmarroco'))
