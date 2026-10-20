
from collections import deque
import heapq

labirinto = [
    "I......#..",
    ".###.###..",
    "...#...#..",
    "##.#.#.#..",
    "...#.#....",
    ".###.####.",
    ".....#....",
    ".###.#.##.",
    "...#......",
    "##.......F"
]

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))


def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'


def montar_grafo(lab):
    grafo = {}

    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue

            grafo[(i, j)] = []

            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))

    return grafo


def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]

    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'

    for linha in grade:
        print(''.join(linha))


def montar_caminho(pais, fim):
    caminho = []
    atual = fim

    while atual is not None:
        caminho.append(atual)
        atual = pais[atual]

    return caminho[::-1]


def dfs(grafo, inicio, saida):
    pilha = [inicio]
    pais = {inicio: None}
    visitados = set()

    while pilha:
        atual = pilha.pop()

        if atual in visitados:
            continue

        visitados.add(atual)

        if atual == saida:
            return montar_caminho(pais, saida), len(visitados)

        for vizinho in grafo[atual]:
            if vizinho not in pais:
                pais[vizinho] = atual
                pilha.append(vizinho)

    return [], len(visitados)


def bfs(grafo, inicio, saida):
    fila = deque([inicio])
    pais = {inicio: None}
    visitados = 0

    while fila:
        atual = fila.popleft()
        visitados += 1

        if atual == saida:
            return montar_caminho(pais, saida), visitados

        for vizinho in grafo[atual]:
            if vizinho not in pais:
                pais[vizinho] = atual
                fila.append(vizinho)

    return [], visitados


def gulosa(grafo, inicio, saida):
    def distancia(pos):
        return abs(pos[0] - saida[0]) + abs(pos[1] - saida[1])

    fila = [(distancia(inicio), 0, inicio)]
    pais = {inicio: None}
    visitados = set()
    ordem = 0

    while fila:
        _, _, atual = heapq.heappop(fila)

        if atual in visitados:
            continue

        visitados.add(atual)

        if atual == saida:
            return montar_caminho(pais, saida), len(visitados)

        for vizinho in grafo[atual]:
            if vizinho not in pais:
                pais[vizinho] = atual
                ordem += 1
                heapq.heappush(
                    fila,
                    (distancia(vizinho), ordem, vizinho)
                )

    return [], len(visitados)


grafo = montar_grafo(labirinto)
inicio = achar(labirinto, 'I')
saida = achar(labirinto, 'F')

for nome, busca in [
    ('DFS', dfs),
    ('BFS', bfs),
    ('Gulosa', gulosa)
]:
    caminho, visitadas = busca(grafo, inicio, saida)

    print('\n', nome)
    desenhar(labirinto, caminho)

    if caminho:
        print('Passos:', len(caminho) - 1)
    else:
        print('Caminho nao encontrado')

    print('Casas visitadas:', visitadas)
