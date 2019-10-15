# nome_do_arquivo_de_entrada = input('Digite o nome do entrada de entrada: ')
# nome_do_arquivo_de_saida = input('Digite o nome do entrada de saída: ')
import struct

nome_do_arquivo_de_entrada = 'valores.bin'
arquivo_entrada = open(nome_do_arquivo_de_entrada, 'rb')


def para_int(quatro_bytes: bytes) -> int:
    return struct.unpack('i', quatro_bytes)[0]


def mdc(primeiro_numero, segundo_numero):
    if segundo_numero == 0:
        return primeiro_numero
    return mdc(segundo_numero, primeiro_numero % segundo_numero)


with arquivo_entrada as entrada:
    numero_de_pares = para_int(arquivo_entrada.read(4))
    print(f'Número de pares={numero_de_pares}')
    for _ in range(numero_de_pares):
        primeiro_numero = para_int(arquivo_entrada.read(4))
        segundo_numero = para_int(arquivo_entrada.read(4))
        print(mdc(primeiro_numero, segundo_numero))
