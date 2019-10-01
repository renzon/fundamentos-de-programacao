def palindromo(palavra: str) -> bool:
    if len(palavra) <= 1:
        return True
    primeira_letra = palavra[0]
    ultima_letra = palavra[-1]
    if primeira_letra != ultima_letra:
        return False
    return palindromo(palavra[1:-1])


nome_do_arquivo = input('Digite o nome do arquivo de entrada: ')
with open(nome_do_arquivo, 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        palavras = linha.split()
        for palavra in palavras:
            if palindromo(palavra):
                print(palavra)

# print(palindromo('ama'))
# print(palindromo('socorrammesubinoonibusemmarroco'))
