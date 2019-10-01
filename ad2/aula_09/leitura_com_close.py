arquivo = open('exemplo.txt', 'r', encoding='utf8')

for linha in arquivo:
    print(linha.strip())

arquivo.close()
