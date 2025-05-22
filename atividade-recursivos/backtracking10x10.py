labirinto = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]

caminho = []

def resolver(x, y):
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    if x < 0 or y < 0 or x >= linhas or y >= colunas:
        return False
    if labirinto[x][y] != 0:
        return False

    caminho.append((x, y))

    if (x, y) == (linhas - 1, colunas - 1):
        print("Chegou à saída!")
        return True

    labirinto[x][y] = 2

    if (resolver(x+1, y) or resolver(x-1, y) or
        resolver(x, y+1) or resolver(x, y-1)):
        return True

    caminho.pop()
    return False

resolver(0, 0)
print("Caminho até a saída:", caminho)
