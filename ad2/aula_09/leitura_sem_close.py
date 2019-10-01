with open('exemplo.txt', 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        print(linha.strip())
