# Projeto 2 de Teoria e Aplicação de Grafos 2022/2
# Henrique Rodrigues Rocha — 211036061

# Python - 3.11
def main():
    professores, habilitacoes, vagas = grafo_bipartido('entradaProj2TAG.txt', 100, 50)
    emparelhamento = emparelhar_grafo(professores, habilitacoes, vagas)

    for escola in emparelhamento:
        print(f'{escola}: {emparelhamento[escola]}')


# Gera, a partir de um grafo bipartido com conjuntos independentes de m professores e n escolas, carregado de um
# arquivo com o mesmo formato que o 'entradaProj2TAG.txt'. O grafo é separado em três dicionários para facilitar a
# aplicação do algoritmo de emparelhamento.
def grafo_bipartido(caminho, m, n):
    professores = {}
    habilitacoes = {}
    vagas = {}

    with open(caminho, 'r') as arquivo:
        linhas = arquivo.read().splitlines()
        j = 0

        for i in range(len(linhas)):
            if linhas[i].startswith('//') or len(linhas[i]) == 0:
                continue

            if j < m:
                vertice, adjacentes = linhas[i].split(': ')
                professor, habilitacao = vertice.strip('()').split(', ')
                preferencias_professor = adjacentes.strip('()').split(', ')

                professores[professor] = tuple(preferencias_professor)
                habilitacoes[professor] = habilitacao
            elif j < m + n:
                vertice, *adjacentes = linhas[i].split(':')
                escola = vertice.strip('()')
                vagas_escola = [adjacente.strip('()') for adjacente in adjacentes]

                vagas[escola] = tuple(vagas_escola)
            else:
                break

            j += 1

    return professores, habilitacoes, vagas


# Encontra um emparelhamento estável entre professores e escolas, com base nas preferências e vagas disponíveis.
# Aplica o algoritmo Gale-Shapley adaptado para o problema, seguindo a solução de  (Abraham, Irving & Manlove, 2007).
def emparelhar_grafo(professores, habilitacoes, vagas) -> dict:
    pass


# Chamada da função principal (esse arquivo é um script).
if __name__ == '__main__':
    main()
