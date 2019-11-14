# AP2 - Questão 3

# Subprogramas


def lerLista():
    import struct
    with open("entrada.bin", "rb") as arq:
        n = struct.unpack("i", arq.read(4))[0]
        valores = []
        for i in range(n):
            valores.append(struct.unpack("d", arq.read(8))[0])
    return valores


def encontrar_minimo(lista):
    menor = lista[0]
    menor_i = 0
    for i, valor in enumerate(lista):
        if valor < menor:
            menor = valor
            menor_i = i

    return menor_i, menor


def ordenarLista(lista):
    valores = []

    while len(lista) > 0:
        i, valor = encontrar_minimo(lista)
        valores.append(valor)
        lista.pop(i)

    # for i in range(0, len(lista) - 1):
    #     menor = i
    #     for k in range(i + 1, len(lista)):
    #         if lista[k] < lista[menor]:
    #             menor = k
    #     lista[menor], lista[i] = lista[i], lista[menor]
    return valores


def escreverLista(lista):
    import struct
    with open("saida.bin", "wb") as arq:
        arq.write(struct.pack("i", len(lista)))
        for v in lista:
            arq.write(struct.pack("d", v))


# Programa Principal
valores = lerLista()
valores = ordenarLista(valores)
escreverLista(valores)
