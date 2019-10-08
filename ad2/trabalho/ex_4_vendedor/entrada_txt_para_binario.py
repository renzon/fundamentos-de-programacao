import struct

entrada_txt = open('entrada.txt', 'r', encoding='utf8')
saida_bin = open('entrada.bin', 'wb')
with entrada_txt as entrada, saida_bin as saida:
    for linha in entrada:
        linha = linha.strip()
        inteiros = [int(s) for s in linha.split()]
        for inteiro in inteiros:
            saida.write(struct.pack('i', inteiro))
