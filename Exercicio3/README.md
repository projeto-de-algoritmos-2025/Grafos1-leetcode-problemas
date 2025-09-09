# Exercício 3: Sum of Distances in Tree (Difícil)

Este diretório contém a solução para o terceiro exercício da disciplina de Grafos 1, baseado no problema "Sum of Distances in Tree" do LeetCode.

## Descrição
O objetivo do exercício é, dado um grafo em forma de árvore com n nós rotulados de 0 a n - 1, calcular para cada nó a soma das distâncias entre esse nó e todos os outros nós da árvore.

## Enunciado

[Link do Exercício](https://leetcode.com/problems/sum-of-distances-in-tree/)

Dado um inteiro n representando o número de nós da árvore e um array edges onde edges[i] = [ai, bi] indica que existe uma aresta entre os nós ai e bi, retorne um array answer de comprimento n onde answer[i] é a soma das distâncias entre o nó i e todos os outros nós.

✅ Exemplo

**Entrada:**

```
n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
```

**Saída:**

```
[8,12,6,10,10,10]
```

## Status da Resolução
![Solução Exercício 3](../Imagens/Exercicio3-Solucao.png)