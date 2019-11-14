# AP2 - Questão 3 - Programa auxiliar para criar arquivos binários no formato especificado

import struct

with open("entrada.bin", "wb") as arq:
    n = int(input("Informe a quantidade de números desejada: "))
    arq.write(struct.pack("i", n))
    for i in range(n):
        v = float(input("Informe o número %d/%d: " % ((i + 1), n)))
        arq.write(struct.pack("d", v))
