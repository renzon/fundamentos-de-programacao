with open('saida.txt', 'w', encoding='utf8') as arquivo:
    for fruta in 'maçã banana abacaxi'.split():
        arquivo.write(f'{fruta}\n')
