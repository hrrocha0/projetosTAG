# Função principal que realiza os itens presentes na descrição do projeto.
# TODO: melhorar o código
def main():
    grafo = gerar_grafo('cliques_copas.txt')
    cliques_maximais = bron_kerbosch(list(grafo.keys()), [], [], grafo)
    cliques_min_3 = filter(lambda c: len(c) >= 3, cliques_maximais)  # TODO: >3 ou >=3?

    for clique in cliques_min_3:
        print(clique)

    print(clique_maximo(cliques_maximais))


# Gera um grafo na representação de lista de adjacência a partir de um arquivo.
def gerar_grafo(caminho):
    grafo = {}

    with open(caminho, 'r') as arquivo:
        linhas = arquivo.read().splitlines()

        for linha in linhas:
            if linha.startswith('%') or len(linha) == 0:
                continue

            linha = linha.strip('; ')
            vertice, adjacentes = linha.split(': ')
            grafo[vertice] = adjacentes.split(', ')

    return grafo


# TODO: Referencia (encontrar um algoritmo aleatorio pra ser a fonte)
# TODO: comentar saidas intermediarias (?)
# Aplica o algoritmo Bron-Kerbosch com pivoteamento no grafo para encontrar seus cliques maximais.
def bron_kerbosch(p, r, x, grafo):
    if len(p) == len(x) == 0:
        return [r]

    pivo = escolher_pivo(p + x, grafo)
    vizinhos_pivo = vizinhos(pivo, grafo)
    resultado = []

    for v in complemento(p, vizinhos_pivo):
        vizinhos_v = vizinhos(v, grafo)
        resultado += bron_kerbosch(intersecao(p, vizinhos_v), r + [v], intersecao(x, vizinhos_v), grafo)
        p.remove(v)
        x.append(v)

    return resultado


def coeficiente_aglomeracao(grafo):
    pass


# Retorna a interseção de duas listas 'a' e 'b'.
def intersecao(a, b):
    return [x for x in a if x in b]


# Retorna o complemento da lista 'b' na lista 'a'.
def complemento(a, b):
    return [x for x in a if x not in b]


# Retorna o clique máximo, dados os cliques maximais.
def clique_maximo(cliques):
    return max(cliques, key=lambda c: len(c))


# Escolhe como pivô o vértice da lista 'vertices' de maior grau no grafo.
def escolher_pivo(vertices, grafo):
    pivo = vertices[0]

    for vertice in vertices:
        if grau(vertice, grafo) > grau(pivo, grafo):
            pivo = vertice

    return pivo


# Retorna os vizinhos de um vértice no grafo.
def vizinhos(vertice, grafo):
    if vertice not in grafo:
        return []

    return grafo[vertice]


# Retorna o grau de um vértice no grafo.
def grau(vertice, grafo):
    if vertice not in grafo:
        return 0

    return len(grafo[vertice])


# Chamada da função principal. Esse arquivo é um script Python 3.11.
if __name__ == '__main__':
    main()
