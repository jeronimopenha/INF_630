def mochila_com_repeticao(
    itens: list,
    capacidade: int,
    item_idx: int,
    tabela: dict

) -> list(list()):
    w_item = itens[item_idx][0]
    v_item = itens[item_idx][1]
    if item_idx <= 0 or capacidade <= 0:
        return 0

    if tabela[item_idx][capacidade] is None:
        r1 = mochila_com_repeticao(itens, capacidade, item_idx-1, tabela)
        if capacidade - w_item >= 0:
            r2 = v_item+mochila_com_repeticao(
                itens, capacidade-w_item, item_idx, tabela)
            r = max(r1, r2)
        else:
            r = r1
        tabela[item_idx][capacidade] = r
        return r
    else:
        r = tabela[item_idx][capacidade]
        return r


# Usei o exemplo do exercicio LEV 8.2 1a para testar o algoritmo
# vetor de vetores no padrao:idx = item, [peso, valor]
#capacidade = 5
#itens = [[0, 0], [2, 12], [1, 10], [3, 20], [2, 15]]
capacidade = 6
itens = [[0, 0], [3, 25], [2, 20], [1, 15], [4, 40], [5, 50]]

n_itens = len(itens)
tabela = [[None for i in range(capacidade+1)]for i in range(n_itens)]
solucao = mochila_com_repeticao(itens, capacidade, n_itens-1, tabela)
print(solucao)
