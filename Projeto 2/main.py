# Projeto 2 de Teoria e Aplicação de Grafos 2022/2
# Henrique Rodrigues Rocha — 211036061

# Python - 3.11
def main():
    preferencias, habilitacoes, vagas = grafo_bipartido('entradaProj2TAG.txt', 100, 50)
    emparelhamento = alocar_professores(preferencias, habilitacoes, vagas)

    print('----------------------------------------------------------------------')
    print('Emparelhamento:')

    for escola in emparelhamento:
        print(f'{escola}: {" ".join(filter(lambda p: p is not None, emparelhamento[escola]))}')

    print('----------------------------------------------------------------------')

    print(f'{professores_alocados(preferencias, emparelhamento)} professores podem ser alocados estavelmente.')


# Gera, a partir de um grafo bipartido com conjuntos independentes de m professores e n escolas, carregado de um
# arquivo com o mesmo formato que o 'entradaProj2TAG.txt'. O grafo é separado em três dicionários para facilitar a
# aplicação do algoritmo de emparelhamento.
# O arquivo foi alterado para remover barras de espaço em excesso e facilitar a leitura.
def grafo_bipartido(caminho, m, n):
    preferencias = {}
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

                preferencias[professor] = preferencias_professor
                habilitacoes[professor] = habilitacao
            elif j < m + n:
                vertice, *adjacentes = linhas[i].split(':')
                escola = vertice.strip('()')
                vagas_escola = [adjacente.strip('()') for adjacente in adjacentes]

                vagas[escola] = vagas_escola
            else:
                break

            j += 1

    return preferencias, habilitacoes, vagas


# Encontra um emparelhamento estável entre professores e escolas, com base nas preferências e vagas disponíveis.
# Aplica a solução SPA-student de (Abraham, Irving & Manlove, 2007), que utiliza o algoritmo Gale-Shapley, adaptando-se para este problema.
def alocar_professores(preferencias, habilitacoes, vagas):
    professores = list(preferencias.keys())
    escolas = list(vagas.keys())
    emparelhamento = {escola: [None for _ in vagas[escola]] for escola in escolas}
    emparelhado = {professor: False for professor in professores}
    _preferencias = {p: preferencias[p].copy() for p in professores}

    while True:
        professor = next(filter(lambda p: not emparelhado[p] and len(_preferencias[p]) > 0, professores), None)

        if professor is None:
            break

        habilitacao = habilitacoes[professor]

        for i in [0, 1]:
            if not emparelhado[professor]:
                for preferencia in _preferencias[professor]:
                    if len(vagas[preferencia]) > i:
                        vaga = vagas[preferencia][i]
                        p = emparelhamento[preferencia][i]

                        if p is None:
                            emparelhamento[preferencia][i] = professor
                            emparelhado[professor] = True
                            break
                        if habilitacao == vaga and habilitacoes[p] != vaga:
                            emparelhamento[preferencia][i] = professor
                            emparelhado[professor] = True
                            emparelhado[p] = False
                            break

        if not emparelhado[professor]:
            emparelhado[professor] = True

    return emparelhamento


# Calcula quantos professores foram alocados estavelmente.
def professores_alocados(preferencias, emparelhamento):
    professores_alocados = 0

    for professor in preferencias:
        for preferencia in preferencias[professor]:
            if professor in emparelhamento[preferencia]:
                professores_alocados += 1
                break

    return professores_alocados


# Chamada da função principal (esse arquivo é um script).
if __name__ == '__main__':
    main()
