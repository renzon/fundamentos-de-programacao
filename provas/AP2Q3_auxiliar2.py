# AP2 - Questão 3 - Programa auxiliar para mostrar arquivos binários no formato especificado

import struct

with open("saida.bin", "rb") as arq:
    n = struct.unpack("i", arq.read(4))[0]
    print(n)
    for i in range(n):
        print(struct.unpack("d", arq.read(8))[0])
