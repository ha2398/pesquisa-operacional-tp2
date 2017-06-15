# Pesquisa Operacional - Trabalho Prático 2 - 1º Semestre de 2017 - UFMG/DCC

**Autor**: [Hugo Sousa](https://github.com/ha2398)

## Descrição

Dois algoritmos são implementados nesse trabalho.

1. Algoritmo de aproximação primal-dual para o problema de cobertura por conjuntos.
1. [Método guloso de Ford-Fulkerson](https://pt.wikipedia.org/wiki/Algoritmo_de_Ford-Fulkerson) para achar um fluxo máximo em grafos direcionados.

## Entrada

1. Cobertura por conjuntos:
	1. Matriz N cujas linhas são indexadas por elementos, e colunas por subconjuntos. Uma entrada será 1 se o elemento pertencer ao conjunto, 0 caso contrário.
	1. Vetor c que indica o custo de cada subconjunto.
	1. Formato: arquivo txt contendo apenas números, espaços e line-breaks. Primeira linha: quantidade de elementos. Segunda linha: quantidade de subconjuntos. Terceira linha: vetor c, cujas entradas serão separadas somente por espaços. Linhas seguintes: matriz N, com entradas de cada linha separadas por espaços, e linhas de N separadas por line-breaks.
1. Ford-Fulkerson:
	1. Matriz N, de incidência do grafo dirigido. Assuma que a fonte do fluxo será o primeiro vértice de N, e o sorvedouro será o último vértice.
	1. Vetor c, de números inteiros, que indica a capacidade de cada arco.
	1. Formato: arquivo txt contendo apenas números, espaços e line-breaks. Primeira linha: quantidade de vértices. Segunda linha: quantidade de arcos. Terceira linha: vetor c, cujas entradas serão separadas somente por espaços. Linhas seguintes: matriz N, com entradas de cada linha separadas por espaços e linhas de N separadas separadas por line-breaks.

## Saída

Em ambos os casos, os algoritmos fornecerão saídas a cada iteração.

1. Cobertura por conjuntos:
	1. Cada iteração do algoritmo produz dois vetores. Um vetor y, inteiro, de 0s e 1s, que é inicializado como todos 0s e se torna uma solução viável da dual apenas na última iteração; e um vetor x, não negativo, inicializado com 0s, e que é sempre viável para a dual do problema.
	1. A cada iteração do algoritmo, será impresso o vetor y em uma linha, o vetor x na linha seguinte, e duas linhas em branco. Os valores decimais são arredondados para três casas decimais.
	1. Após a última iteração, também será impresso o custo da cobertura encontrada.
1. Ford-Fulkerson:
	1. A cada iteração, será impresso o vetor 0s e 1s que indica qual caminho está sendo considerado, uma linha em branco, o vetor dos novos fluxos obtidos após a iteração, linha em branco, uma cópia do vetor c original e duas linhas em branco. Todos esses vetores têm dimensão igual ao número de arcos.
	1. Após a última iteração, será impresso o valor máximo do fluxo encontrado e uma linha em branco.
	1. Após o valor do fluxo máximo, será impresso um vetor de 0s e 1s que indique um st-corte mínimo do grafo.
	1. Todos os números serão inteiros.

## Execução

Para executar o programa, o seguinte comando deve ser executado:

python3 tp2.py <algoritmo> <entrada> <saida>

Onde <algoritmo> indica o algoritmo desejado (cobertura por conjuntos ou ford-fulkerson), <entrada> indica o nome do arquivo que contém os dados de entrada e <saida> representa o nome do arquivo onde toda a saída do programa será escrita.

## Observações

Desenvolvido usando Python 3 (3.4.3) como referência.
