# nome_do_arquivo = input('Digite o nome do entrada de entrada: ')
nome_do_arquivo = 'entrada.txt'
conjunto_palavras_caracteres_repetidos = set()
with open(nome_do_arquivo, 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        palavras = linha.split()
        for palavra in palavras:
            palavra = palavra.strip()
            caracteres_nao_repetidos = set(palavra)
            if len(palavra) > len(caracteres_nao_repetidos):
                conjunto_palavras_caracteres_repetidos.add(palavra)

if len(conjunto_palavras_caracteres_repetidos) == 0:
    print('Nenhuma palavra com caracteres repetidos foi encontrada!!!')
else:
    print(f'Palavras com caracteres repetidos = {conjunto_palavras_caracteres_repetidos}')
