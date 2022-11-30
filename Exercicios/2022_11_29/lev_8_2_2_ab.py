def mochila(
    itens: list[list[int]],
    n_itens: int,
    capacidade: int
) -> list[list[int]]:
    # matriz 2d inicialmente preenchida com 0
    solucao = [[0 for i in range(capacidade+1)]for i in range(n_itens+1)]
    for i in range(n_itens):
        item_w = itens[i][0]
        item_v = itens[i][1]
        for j in range(capacidade):
            if j + 1 - item_w < 0:
                solucao[i+1][j+1] = solucao[i][j+1]
            else:
                solucao[i+1][j+1] = max(
                    item_v+solucao[i][j+1-item_w],
                    solucao[i][j+1]
                )
    return solucao


def selecionar_itens(
    solucao: list[list[int]],
    itens: list[list[int]],
    n_itens: int,
    capacidade: int
) -> list[int]:
    itens_escolhidos = {}
    j = capacidade
    i = n_itens-1
    while(j > 0 and i+1 > 0):
        v = solucao[i+1][j]
        if v == solucao[i][j]:
            i -= 1
            continue
        else:
            itens_escolhidos[str(i+1)] = itens[i]
            j -= itens[i][0]
            i -= 1
    return itens_escolhidos


# Usei o exemplo do exercicio LEV 8.2 1a para testar o algoritmo
# vetor de vetores no padrao:idx = item, [peso, valor]
#capacidade = 5
#itens = [[2, 12], [1, 10], [3, 20], [2, 15]]
capacidade = 6
itens = [[3, 25], [2, 20], [1, 15], [4, 40], [5, 50]]

n_itens = len(itens)
solucao = mochila(itens, n_itens, capacidade)
itens_selecionados = selecionar_itens(solucao, itens, n_itens, capacidade)
print(itens_selecionados)
