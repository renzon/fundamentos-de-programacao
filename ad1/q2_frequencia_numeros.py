def ler_numeros():
    numeros_str = '1 2 3 4 3 2 9 7 8 5.5 3 9 8 3 9 9 9 8 8 8 8'  # input('Digite numeros separados por espaço: ')
    numeros = [float(s) for s in numeros_str.split()]
    return numeros


numeros = ler_numeros()
quantidade_de_numeros = len(numeros)  # quantidade_de_numeros = 2


def retornar_numero_com_maior_frequencia(numeros):
    # frequencias = [
    #     # [1, 1],
    #     # [2, 2],
    #     # [4, 3],
    #     # [1, 4],
    #     # [3, 9],
    #     # [2, 8],
    #     # [1, 5.5],
    # ]
    #
    # for n in numeros:  # n=6
    #     flag_numero_encontrado = False
    #     for frequencia_numero in frequencias:
    #         if n == frequencia_numero[1]:
    #             frequencia_numero[0] += 1
    #             flag_numero_encontrado = True
    #             break
    #     if not flag_numero_encontrado:
    #         frequencia_numero = [1, n]
    #         frequencias.append(frequencia_numero)

    frequencias = {}
    for n in numeros:
        freq_n = frequencias.get(n, 0)
        freq_n += 1
        frequencias[n] = freq_n
    invertido=[(valor, chave) for chave, valor in frequencias.items()]
    return max(invertido)


if quantidade_de_numeros == 0:
    print('nenhum número foi lido!!!')
else:
    frequencia, numero = retornar_numero_com_maior_frequencia(numeros)
    print(f'Valor que mais ocorreu: {numero} que foi encontrado: {frequencia} vez(es)')
