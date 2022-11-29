# minimum-sum descent forca bruta
def msd_fb(p: list([list([int])]), i: int, j: int) -> int:
    if i == 0:
        return p[i][j]
    else:
        r1 = msd_fb(p, i-1, j)
        r2 = msd_fb(p, i-1, j-1)
        r = min(r1, r2)
        s = p[i][j] + r
        return s

# minimum-sum descent programacao dinamica


def msd_pd(p: list([list([int])]), i: int, j: int, tabela: list([list([int])])) -> int:
    if i == 0:
        return p[i][j]
    else:
        if tabela[i-1][j] is None:
            r1 = msd_pd(p, i-1, j, tabela)
            tabela[i-1][j] = r1
        else:
            r1 = tabela[i-1][j]
        if tabela[i-1][j-1] is None:
            r2 = msd_pd(p, i-1, j-1, tabela)
            tabela[i-1][j-1] = r2
        else:
            r2 = tabela[i-1][j-1]
        r = min(r1, r2)
        s = p[i][j] + r
        return s

# minimum-sum descent guloso
def msd_gl(p: list([list([int])]), i: int, j: int) -> int:
    if i == 0:
        return p[i][j]
    if (p[i-1][j]) < p[i-1][j-1]:
        r = msd_gl(p, i-1, j)
        s = p[i][j] + r
        return s
    else:
        r = msd_gl(p, i-1, j-1)
        s = p[i][j] + r
        return s


p = [
    [6, 9, 6, 8],
    [0, 7, 4, 1],
    [0, 0, 4, 5],
    [0, 0, 0, 2],


]
n = len(p)
tabela = [[None for i in range(n)] for i in range(n)]
i = n-1
j = n-1
print(msd_fb(p, i, j))
print(msd_pd(p, i, j,tabela))
print(msd_gl(p, i, j))
