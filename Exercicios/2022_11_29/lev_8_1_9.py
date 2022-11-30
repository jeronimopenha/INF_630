def coeficiente_binomial(n: int, k: int, tabela: list[list[int]]) -> int:
    if n == k or k == 0:
        return 1
    if tabela[n-1][k-1] is None:
        r1 = coeficiente_binomial(n-1, k-1, tabela)
        tabela[n-1][k-1] = r1
    else:
        r1 = tabela[n-1][k-1]
    if tabela[n-1][k] is None:
        r2 = coeficiente_binomial(n-1, k, tabela)
        tabela[n-1][k] = r2
    else:
        r2 = tabela[n-1][k]
    r = r1+r2
    return r


n = 9
k = 3
tabela = [[None for i in range(k+1)] for i in range(n+1)]
print(coeficiente_binomial(n, k, tabela))
