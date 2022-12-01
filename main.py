# Função principal que realiza os itens presentes na descrição do projeto.
def main():
    grafo = gerar_grafo('cliques_copas.txt')
    maximais = cliques_maximais(grafo)
    cliques_min_3 = [c for c in maximais if len(c) >= 3]  # TODO: >3 ou >=3?
    print('----------------------------------------------------------------------')
    print('Cliques acima de 3 vértices:')

    for clique in cliques_min_3:
        print(f'{clique} - {len(clique)} vértices')

    print('----------------------------------------------------------------------')
    print(f'Clique máximo: {clique_maximo(maximais)}')
    print('----------------------------------------------------------------------')
    print(f'Coeficiente de aglomeração médio: {coeficiente_aglomeracao(grafo)}')


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


# Retorna uma lista contendo todos os cliques maximais do grafo.
def cliques_maximais(grafo):
    return bron_kerbosch(list(grafo.keys()), [], [], grafo)


# Retorna o clique máximo, dados os cliques maximais.
def clique_maximo(cliques):
    return max(cliques, key=lambda c: len(c))


# Encontra o coeficiente de agrupamento médio do grafo.
def coeficiente_aglomeracao(grafo):
    return sum([aglomeracao_vertice(v, grafo) for v in grafo]) / len(grafo)


# TODO: Referencia (encontrar um algoritmo aleatorio pra ser a fonte)
def bron_kerbosch(p, r, x, grafo):
    if len(p) == len(x) == 0:
        print(r)
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


# Escolhe como pivô o vértice da lista 'vertices' de maior grau no grafo.
def escolher_pivo(vertices, grafo):
    pivo = vertices[0]

    for vertice in vertices:
        if grau(vertice, grafo) > grau(pivo, grafo):
            pivo = vertice

    return pivo


# Encontra o coeficiente de aglomeração de um vértice.
def aglomeracao_vertice(vertice, grafo):
    v = vizinhos(vertice, grafo)
    n = grau(vertice, grafo)
    t = 0
    verificados = []

    if n < 2:
        return 0

    for v1 in v:
        for v2 in complemento(v, verificados + [v1]):
            if v2 in grafo[v1]:
                t += 1

        verificados.append(v1)

    return (2 * t) / (n * (n - 1))


# Retorna a interseção de duas listas 'a' e 'b'.
def intersecao(a, b):
    return [x for x in a if x in b]


# Retorna o complemento da lista 'b' na lista 'a'.
def complemento(a, b):
    return [x for x in a if x not in b]


# Retorna o grau de um vértice no grafo.
def grau(vertice, grafo):
    if vertice not in grafo:
        return 0

    return len(grafo[vertice])


# Retorna os vizinhos de um vértice no grafo.
def vizinhos(vertice, grafo):
    if vertice not in grafo:
        return []

    return grafo[vertice]


# Chamada da função principal. Esse arquivo é um script Python 3.11.
if __name__ == '__main__':
    main()
