def ler_numeros():
    numeros = []  # numeros = [ 4.0, 5.0 ]
    while True:
        numero = input('Digite um número ou aperte enter para finalizar: ')
        if numero == '':
            break
        else:
            numero = float(numero)
            numeros.append(numero)
    return numeros


numeros = ler_numeros()

quantidade_de_numeros = len(numeros)  # quantidade_de_numeros = 2
print(f'Quantidade de numeros inseridos: {quantidade_de_numeros}')

if quantidade_de_numeros == 0:
    print('Não é possível calcular média e máximo pois não foi inserido nenhum valor')
else:
    candidato_a_maximo = numeros[0]  # candidato_a_maximo = 2
    for n in numeros:  # n = 1
        if candidato_a_maximo < n:  # [1, 2, 1]
            candidato_a_maximo = n
    print(f'Valor máximo inserido foi {candidato_a_maximo}')
    media = sum(numeros) / quantidade_de_numeros  # 9 / 2 = 4.5
    print(f'A média dos valores inserido é {media}')
