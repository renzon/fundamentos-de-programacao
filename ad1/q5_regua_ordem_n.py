def escrever_regua(n: int) -> None:  # n =1
    inicio = 1
    final = 2 ** n
    escrever_regua_recursiva(final, inicio, n)


def escrever_regua_recursiva(final, inicio, n):
    if n == 0:
        return
    final -= 1
    ponto_medio = (final + inicio) // 2
    escrever_regua_recursiva(ponto_medio, inicio, n - 1)
    print(f'{ponto_medio:02} ' + '-' * n)
    escrever_regua_recursiva(final+1, ponto_medio+1, n - 1)


if __name__ == '__main__':
    escrever_regua(5)
