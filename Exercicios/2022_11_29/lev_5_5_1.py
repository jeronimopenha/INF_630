
# closest pair onde dimensional

# força bruta
def par_mais_perto_fb(itens: list[int]) -> list[int, int]:
    it = sorted(itens)
    mais_pertos = [it[0], it[1]]
    menor_distancia = abs(it[0]-it[1])
    for i in range(2, len(it)):
        if abs(it[i]-it[i-1]) < menor_distancia:
            menor_distancia = abs(it[i]-it[i-1])
            mais_pertos = [it[i-1], it[i]]
    return mais_pertos


# dividir pra conquistar

def par_mais_perto_dc(itens: list[int]) -> list[list[int, int], int]:
    n = len(itens)
    if n == 3:
        if abs(itens[0]-itens[1]) < abs(itens[1]-itens[2]):
            return [itens[0], itens[1]], abs(itens[0]-itens[1])
        else:
            return [itens[1], itens[2]], abs(itens[1]-itens[2])
    elif n == 2:
        return [itens[0], itens[1]], abs(itens[0]-itens[1])
    else:
        c1 = itens[:n//2]
        c2 = itens[n//2:]
        p1, p1_dt = par_mais_perto_dc(c1)
        p2, p2_dt = par_mais_perto_dc(c2)
        p3 = [c1[-1], c2[0]]
        p3_dt = abs(p3[0]-p3[1])
        d = min(p1_dt, p2_dt, p3_dt)
        if p1_dt == d:
            return p1, p1_dt
        elif p2_dt == d:
            return p2, p2_dt
        else:
            return p3, p3_dt


itens = [376, 317, 700, 553, 758, 378, 533, 692, 888, 157,
         969, 468, 470, 124, 596, 321, 43, 837, 737, 444,
         356, 898, 907, 8, 34, 881, 140, 632, 937, 401,
         197, 880, 666, 826, 831, 400, 445, 111, 199, 315,
         385, 784, 115, 825, 738, 57, 143, 593, 22, 408,
         639, 159, 516, 867, 511, 300, 233, 573, 209, 868,
         858, 677, 558, 824, 461, 534, 900, 18, 517, 684,
         374, 196, 182, 467, 571, 554, 823, 852, 765, 959,
         782, 622, 841, 403, 304, 976, 997, 173, 866, 303,
         101, 49, 562, 600, 954, 842, 262, 853, 31, 503]

it = sorted(itens)
print(par_mais_perto_fb(it))
print(par_mais_perto_dc(it))
