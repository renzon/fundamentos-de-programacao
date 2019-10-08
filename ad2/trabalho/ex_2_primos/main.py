def eh_primo(n: int) -> bool:
    return True


nome_do_arquivo_de_entrada = input('Digite o nome do entrada de entrada: ')
nome_do_arquivo_de_saida = input('Digite o nome do entrada de saída: ')
arquivo_entrada = open(nome_do_arquivo_de_entrada, 'r', encoding='utf8')
arquivo_saida = open(nome_do_arquivo_de_saida, 'w', encoding='utf8')
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

