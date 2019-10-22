# nome_do_arquivo = input('Digite o nome do entrada de entrada: ')
import os

nome_do_arquivo = 'teste.txt'


def insereOrdenado(nome_do_arquivo: str, novo_valor: float):
    nome_arquivo_temporario = 'temp.txt'
    arquivo_entrada = open(nome_do_arquivo, 'r', encoding='utf8')
    arquivo_temporario = open(nome_arquivo_temporario, 'w', encoding='utf8')
    valor_inserido = False
    with arquivo_entrada as entrada, arquivo_temporario as saida:
        for linha in entrada:
            valor = linha.strip()
            if not valor_inserido and valor != '':
                valor = float(valor)
                if novo_valor < valor:
                    saida.write(f'{novo_valor}\n')
                    valor_inserido = True
                saida.write(linha)
            else:
                saida.write(linha)
        if not valor_inserido:
            saida.write(f'{novo_valor}\n')
    os.remove(nome_do_arquivo)
    os.rename(nome_arquivo_temporario, nome_do_arquivo)


if __name__ == '__main__':
    insereOrdenado(nome_do_arquivo, -3)
