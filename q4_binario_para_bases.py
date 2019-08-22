def transformar_base_2_para_10(n: str) -> int:
    n_reverso = reversed(n)
    numero_base_10 = 0
    for i, algarismo in enumerate(n_reverso):
        algarismo = int(algarismo)
        numero_base_10 += algarismo * (2 ** i)
    return numero_base_10


def converte_base_10(n_base_10: int, base: int):
    algarismos_reversos = []
    divisor = n_base_10
    while True:
        divisor, resto = divmod(divisor, base)
        algarismos_reversos.append(str(resto))
        if divisor == 0:
            break
    return ''.join(reversed(algarismos_reversos))


def converte(n_binario: str, base: int):
    return converte_base_10(transformar_base_2_para_10(n_binario), base)


def converte_base_3_a_10(b_binario):
    conversoes = []
    for base in range(3, 11):
        conversoes.append(converte(b_binario, base))
    return conversoes


while True:
    n = input('Digite um valor binário, ou -1 para finalizar: ')
    if n == '-1':
        break
    print(*converte_base_3_a_10(n))
