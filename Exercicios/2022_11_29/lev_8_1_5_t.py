'''
Applies dynamic programming to compute the largest number of
coins a robot can collect on an n x m board by starting at (1, 1)
and moving right and down from upper left to down right corner
Input: Matrix C[1..n, 1..m] whose elements are equal to 1 and 0
for cells with and without a coin, respectively
Output: Largest number of coins the robot can bring to cell (n, m)
'''

#TESTES!!!!!!!

def robo_coletor_moedas(c: list[list[int]], tabela: list[list[int]], n: int, m: int, i: int, j: int) -> int:
    if i == 0 or j == 0:
        return 0

    if tabela[i-1][j] == -1:
        if c[i-1][j] == 2:
            r1 = 0
        else:
            r1 = robo_coletor_moedas(c, tabela, n, m, i-1, j)
        tabela[i-1][j] = r1
    else:
        r1 = tabela[i-1][j]

    if tabela[i][j-1] == -1:
        if c[i][j-1] == 2:
            r2 = 0
        else:
            r2 = robo_coletor_moedas(c, tabela, n, m, i, j-1)
        tabela[i][j-1] = r2
    else:
        r2 = tabela[i][j-1]
    r = max(r1, r2)
    s = r + c[i][j]
    return s


o = 0

if o == 0:
    c = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 1, 0, 0],
        [0, 1, 0, 0, 2, 1, 0],
        [0, 0, 1, 0, 2, 1, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 2, 2, 2, 0, 1, 0]
    ]
else:
    c = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0]
    ]

n = len(c)
m = len(c[0])
i = n-1
j = m-1
tabela = [[-1 for i in range(m)]for i in range(n)]
tabela[n-1][m-1] = robo_coletor_moedas(c, tabela, n, m, i, j)
print(tabela[n-1, m-1])
