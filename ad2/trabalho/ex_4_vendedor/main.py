# nome_do_arquivo_de_entrada = input('Digite o nome do entrada de entrada: ')
# nome_do_arquivo_de_saida = input('Digite o nome do entrada de saída: ')
import struct

nome_do_arquivo_de_entrada = 'entrada.bin'
nome_do_arquivo_de_saida = 'saida.bin'
arquivo_entrada = open(nome_do_arquivo_de_entrada, 'rb')
arquivo_saida = open(nome_do_arquivo_de_saida, 'wb')


def para_int(quatro_bytes: bytes) -> int:
    return struct.unpack('i', quatro_bytes)[0]


with arquivo_entrada as entrada, arquivo_saida as saida:
    numero_clientes_visitados_na_semana = para_int(arquivo_entrada.read(4))
    print(f'Q={numero_clientes_visitados_na_semana}')
    numero_clientes_visitados_ultimo_dia = para_int(arquivo_entrada.read(4))
    print(f'E={numero_clientes_visitados_ultimo_dia}')
    clientes_ultimo_dia = set()
    for _ in range(numero_clientes_visitados_ultimo_dia):
        clientes_ultimo_dia.add(para_int(arquivo_entrada.read(4)))
    print(f'Clientes visitados último dia: {clientes_ultimo_dia}')
    for _ in range(numero_clientes_visitados_na_semana):
        cliente = para_int(arquivo_entrada.read(4))
        flag_saida=0 if cliente in clientes_ultimo_dia else 1
        arquivo_saida.write(struct.pack('i', flag_saida))

