def eh_primo(n: int) -> bool:
    return True


# nome_do_arquivo = input('Digite o nome do entrada de entrada: ')
arquivo_entrada = open('entrada.txt', 'r', encoding='utf8')
arquivo_saida = open('saida.txt', 'w', encoding='utf8')
with arquivo_entrada as entrada, arquivo_saida as saida:
    for linha in entrada:
        linha = linha.strip()
        numeros = linha.split()
        numeros_primos=[]
        for n in numeros:
            if eh_primo(int(n)):
                numeros_primos.append(n)
        linha_a_ser_escrita=' '.join(numeros_primos)
        saida.write(f'{linha_a_ser_escrita}\n')

# print(eh_primo('ama'))
# print(eh_primo('socorrammesubinoonibusemmarroco'))
