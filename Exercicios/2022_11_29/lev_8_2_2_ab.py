def mochila(
    itens: list,
    n_itens: int,
    capacidade: int,
    solucao: list(list())
) -> list(list()):
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

# Usei o exemplo do exercicio LEV 8.2 1a para testar o algoritmo
capacidade = 6
# vetor de vetores no padrao:idx = item, [peso, valor]
itens = [[3, 25], [2, 20], [1, 15], [4, 40], [5, 50]]
n_itens = len(itens)
# matriz 2d inicialmente preenchida com 0
solucao = [[0 for i in range(capacidade+1)]for i in range(n_itens+1)]
print(mochila(itens, n_itens, capacidade, solucao))