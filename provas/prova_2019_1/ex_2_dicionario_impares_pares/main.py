# nome_do_arquivo = input('Digite o nome do arquivo de entrada: ')
nome_do_arquivo = 'entrada.txt'
frequencia_de_palavras = {}
with open(nome_do_arquivo, 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        palavras = linha.split()
        for palavra in palavras:
            palavra = palavra.strip()
            frequencia_de_palavras[palavra] = frequencia_de_palavras.get(palavra, 0) + 1

if len(frequencia_de_palavras) == 0:
    print('O dicionário ficou vazio!!!')
else:
    print('Dicionário ordenado pelas palavras:')
    ordenadas_por_palavras=sorted(list(frequencia_de_palavras.items()))
    for palavra, frequencia in ordenadas_por_palavras:
        if frequencia==1:
            print(f'    {palavra} ocorreu 1 vez')
        else:
            print(f'    {palavra} ocorreu {frequencia} vezes')


