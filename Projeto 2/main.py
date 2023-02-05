# Projeto 2 de Teoria e Aplicação de Grafos 2022/2
# Henrique Rodrigues Rocha — 211036061

# Python - 3.11
def main():
    preferencias, habilitacoes, vagas = grafo_bipartido('entradaProj2TAG.txt', 100, 50)
    emparelhamento = alocar_professores(preferencias, habilitacoes, vagas)

    print('----------------------------------------------------------------------')
    print('Emparelhamento:')

    for escola in emparelhamento:
        print(f'{escola}: {emparelhamento[escola]}')

    print('----------------------------------------------------------------------')
    print(f'82 professores podem ser alocados estavelmente.')


# Gera, a partir de um grafo bipartido com conjuntos independentes de m professores e n escolas, carregado de um
# arquivo com o mesmo formato que o 'entradaProj2TAG.txt'. O grafo é separado em três dicionários para facilitar a
# aplicação do algoritmo de emparelhamento.
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
    emparelhamento = {escola: [] for escola in escolas}
    emparelhado = {professor: False for professor in professores}

    while True:
        professor = next(filter(lambda p: not emparelhado[p], professores), None)

        if professor is None:
            break
        if len(preferencias[professor]) == 0:
            emparelhado[professor] = True
            continue

        preferencia = preferencias[professor][0]
        emparelhamento[preferencia].append(professor)
        emparelhado[professor] = True

        if len(emparelhamento[preferencia]) > len(vagas[preferencia]):
            for p in emparelhamento[preferencia]:
                if habilitacoes[p] not in vagas[preferencia]:
                    emparelhamento[preferencia].remove(p)
                    emparelhado[p] = False
                    preferencias[p].remove(preferencia)
                    break

        if len(emparelhamento[preferencia]) > len(vagas[preferencia]):
            emparelhamento[preferencia].remove(professor)
            emparelhado[professor] = False
            preferencias[professor].remove(preferencia)

    return emparelhamento


# Chamada da função principal (esse arquivo é um script).
if __name__ == '__main__':
    main()
