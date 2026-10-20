# Atividade 9 - Labirinto

Atividade de Algoritmos e Estruturas de Dados II com o objetivo de comparar três algoritmos de busca em um labirinto: DFS, BFS e Busca Gulosa.

## Labirinto

Foi criado um labirinto de 10 linhas e 10 colunas, utilizando os seguintes símbolos:

- `I` - Posição inicial
- `F` - Saída do labirinto
- `#` - Parede
- `.` - Caminho livre

```text
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
```

O labirinto possui diferentes caminhos até a saída, além de paredes e becos sem saída que fazem os algoritmos explorarem posições diferentes.

## Implementação

O programa transforma as posições livres do labirinto em um grafo, conectando cada posição às casas disponíveis acima, à direita, abaixo e à esquerda.

Foram implementados três algoritmos:

- **DFS:** utiliza uma lista como pilha, seguindo um caminho até onde conseguir antes de explorar outras possibilidades.
- **BFS:** utiliza uma lista como fila, explorando as posições por níveis e garantindo o menor caminho em quantidade de passos.
- **Busca Gulosa:** utiliza uma lista ordenada pela distância de Manhattan até a saída, priorizando as posições que parecem estar mais próximas do destino.

Os três algoritmos armazenam a posição anterior de cada casa para reconstruir o caminho encontrado.

Na visualização, o símbolo `*` representa as posições que fazem parte do caminho.

## Resultados

| Algoritmo | Passos | Casas visitadas |
|---|---:|---:|
| DFS | 20 | 28 |
| BFS | 18 | 43 |
| Busca Gulosa | 22 | 26 |

A BFS encontrou o menor caminho, com 18 passos, mas precisou visitar mais casas durante a busca. Isso acontece porque ela explora as posições por níveis, verificando diferentes possibilidades antes de chegar à saída.

A DFS encontrou um caminho de 20 passos, pois segue uma direção até onde conseguir antes de voltar e explorar outros caminhos.

Já a Busca Gulosa encontrou um caminho de 22 passos, visitando menos casas que a BFS. Como ela prioriza a distância estimada até a saída, pode acabar escolhendo caminhos que parecem melhores inicialmente, mas que são mais longos por causa das paredes.

No labirinto desenvolvido, a Busca Gulosa priorizou o avanço pela primeira linha, pois isso reduzia a distância estimada até a saída. Porém, as paredes impediram a continuação direta, fazendo o algoritmo explorar um desvio.

Assim, foi possível observar que a BFS garante o menor caminho em um labirinto sem pesos, enquanto a DFS e a Busca Gulosa não possuem essa garantia.

## Execução

Para executar o programa, basta ter o Python instalado e utilizar o comando:

```bash
python main.py
```

O programa mostra o caminho encontrado por cada algoritmo e, ao final, apresenta uma tabela comparando a quantidade de passos e de casas visitadas.

Não é necessário instalar bibliotecas externas.