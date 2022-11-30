'''
Applies dynamic programming to compute the largest number of
coins a robot can collect on an n × m board by starting at (1, 1)
and moving right and down from upper left to down right corner
Input: Matrix C[1..n, 1..m] whose elements are equal to 1 and 0
for cells with and without a coin, respectively
Output: Largest number of coins the robot can bring to cell (n, m)
'''


def robo_coletor_moedas(
    c: list[list[int]],
    tabela: list[list[int]],
    n: int,
    m: int
) -> int:
    tabela[1][1] = c[1][1]
    for j in range(2, m):
        if c[1][j] == 2:
            tabela[1][j] = 0
        else:
            tabela[1][j] = tabela[1][j-1] + c[1][j]
    for i in range(2, n):
        if c[i][1] == 2:
            tabela[i][1] = 0
        else:
            tabela[i][1] = tabela[i-1][1] + c[i][1]
        for j in range(2, m):
            if c[i][j] == 2:
                tabela[i][j] = 0
            else:
                tabela[i][j] = max(tabela[i-1][j], tabela[i][j-1])+c[i][j]
    return tabela[n-1][m-1]


def quantos_caminhos(
        tabela: list[list[int]],
        n: int,
        m: int,
        i: int,
        j: int):
    if j == m-1 and i == n-1:
        # chegou a umtima posicao
        return 1
    if j == m or i == n:
        # saiu dos limites da tabela
        return 0
    r1 = 0
    r2 = 0
    if tabela[i+1][j] < tabela[i][j+1]:
        # vou para a direita
        r1 = quantos_caminhos(tabela, n, m, i, j+1)
        s = r1
    elif tabela[i+1][j] > tabela[i][j+1]:
        # vou para baixo
        r2 = quantos_caminhos(tabela, n, m, i+1, j)
        s = r2
    else:
        # vou para ambos os lados
        r1 = quantos_caminhos(tabela, n, m, i, j+1)
        r2 = quantos_caminhos(tabela, n, m, i+1, j)
        s = r1 + r2
    return s


c = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 1, 0, 0],
    [0, 1, 0, 0, 2, 1, 0],
    [0, 0, 1, 0, 2, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 2, 2, 2, 0, 1, 0]
]

n = len(c)
m = len(c[0])
tabela = [[0 for i in range(m)]for i in range(n)]
solucao = robo_coletor_moedas(c, tabela, n, m)
print(solucao)
i = 1
j = 1
for i in range(n):
    tabela[i].append(0)
tabela.append([0 for i in range(m+1)])
i = 1
j = 1
print(quantos_caminhos(tabela, n, m, i, j))
