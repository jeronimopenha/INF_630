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
    if capacidade - w_item >= 0:
        if '%d,%d' % (item_idx, capacidade) not in tabela.keys():
            r1 = v_item+mochila_com_repeticao(
                itens, capacidade-w_item, item_idx, tabela)
            r2 = mochila_com_repeticao(
                itens, capacidade, item_idx-1, tabela)
            r = max(r2, r1)
            tabela[str('%d,%d' % (item_idx, capacidade))] = r
            return r
        else:
            r = tabela[str('%d,%d' % (item_idx, capacidade))]
            return r
    else:
        return mochila_com_repeticao(
            itens, capacidade, item_idx-1, tabela)


# Usei o exemplo do exercicio LEV 8.2 1a para testar o algoritmo
# vetor de vetores no padrao:idx = item, [peso, valor]
#capacidade = 5
#itens = [[0, 0], [2, 12], [1, 10], [3, 20], [2, 15]]
capacidade = 6
itens = [[0, 0], [3, 25], [2, 20], [1, 15], [4, 40], [5, 50]]

n_itens = len(itens)
solucao = [[None for i in range(capacidade+1)]for i in range(n_itens)]
tabela = {}
mochila_com_repeticao(itens, capacidade, n_itens-1, tabela)
for k in tabela.keys():
    i = int(k.split(',')[0])
    j = int(k.split(',')[1])
    solucao[i][j] = tabela[k]
for l in solucao:
    print(l)
