def main():
    grafo = gerar_grafo('cliques_copas.txt')
    print(grafo)


# Gera um grafo na representação de lista de adjacência a partir de um arquivo
def gerar_grafo(caminho):
    grafo = {}

    with open(caminho, 'r') as arquivo:
        linhas = map(lambda l: l.strip('; '), arquivo.read().splitlines())

        for linha in linhas:
            if linha.startswith('%') or len(linha) == 0:
                continue

            linha = linha.strip('; ')
            vertice, adjacentes = linha.split(': ')
            grafo[vertice] = adjacentes.split(', ')

    return grafo


def bron_kerbosch(p, r, x, grafo):
    pass


# Função auxiliar que escolhe como pivô o vértice da lista 'vertices' de maior grau no grafo
def escolher_pivo(vertices, grafo):
    pivo = vertices[0]

    for vertice in vertices:
        if grau(vertice, grafo) > grau(pivo, grafo):
            pivo = vertice

    return pivo


# Função auxiliar que retorna os vizinhos de um vértice no grafo
def vizinhos(vertice, grafo):
    if vertice not in grafo:
        return []

    return grafo[vertice]


# Função auxiliar que retorna o grau de um vértice no grafo
def grau(vertice, grafo):
    if vertice not in grafo:
        return 0

    return len(grafo[vertice])


def coeficiente_aglomeracao(grafo):
    pass


if __name__ == '__main__':
    main()
