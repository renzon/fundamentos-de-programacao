numeros = []   # numeros = [ 4.0, 5.0 ]

while True:
    numero = input('Digite um número ou aperte enter para finalizar: ')  # numero = ''
    if numero == '':
        break
    else:
        numero = float(numero)
        numeros.append(numero)

quantidade_de_numeros = len(numeros)  # quantidade_de_numeros = 2
print(f'Quantidade de numeros inseridos: {quantidade_de_numeros}')

if quantidade_de_numeros == 0:
    print('Não é possível calcular média e máximo pois não foi inserido nenhum valor')
else:
    maximo = max(numeros)  # maximo = 5.0
    print(f'Valor máximo inserido foi {maximo}')
    media = sum(numeros) / quantidade_de_numeros  # 9 / 2 = 4.5
    print(f'A média dos valores inserido é {media}')
