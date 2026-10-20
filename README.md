# Atividade 9 - Labirinto

Atividade de Algoritmos e Estruturas de Dados II para comparar três formas de buscar a saída de um labirinto: DFS, BFS e Busca Gulosa.

## Labirinto

O labirinto foi criado com 10 linhas e 10 colunas. Nele, `I` é o início, `F` é a saída, `#` representa parede e `.` representa caminho livre.


I......#..
.###.#.#..
...#...#..
##.#.#.#..
..##.#..#.
..##.####.
..#..#....
####.#.##.
...#......
###.....#F


Existem caminhos diferentes até a saída, além de paredes e becos sem saída que fazem os algoritmos explorarem posições diferentes.

## Implementação

O programa transforma as posições livres em um grafo. Cada posição é ligada às casas livres de cima, da direita, de baixo e da esquerda.

- DFS: utiliza uma pilha e tenta seguir um caminho antes de voltar para outras possibilidades.
- BFS: utiliza uma fila e percorre o labirinto por níveis, encontrando o menor caminho em número de passos.
- Busca Gulosa: utiliza uma fila de prioridade e a distância de Manhattan até a saída para escolher a próxima posição.

Os três algoritmos guardam a posição anterior de cada casa para reconstruir o caminho. Na visualização, `*` indica por onde o caminho encontrado passa.

## Resultados

| Algoritmo | Tamanho do caminho (passos) | Casas visitadas |
|---|---:|---:|
| DFS | 20 | 28 |
| BFS | 18 | 43 |
| Busca Gulosa | 22 | 26 |

A BFS encontrou o menor caminho, com 18 passos, mas visitou mais casas. A DFS encontrou uma rota de 20 passos. Já a Busca Gulosa visitou menos casas que a BFS, mas acabou escolhendo um caminho de 22 passos.

A Busca Gulosa se deixou levar pela distância até a saída: na primeira linha, depois de passar pela coluna 4, continuou para a direita até a coluna 6. Essa direção parecia melhor, mas as paredes impediram a continuação direta, fazendo o algoritmo contornar até voltar para a coluna 4 na terceira linha. A BFS não comete esse erro porque busca por níveis, sem priorizar apenas a proximidade da saída.