import random
import time
import traceback

from numpy import append


def sum3_fbruta(vec):
    start = time.time_ns()
    sum3 = []

    qtde_valores = len(vec)

    for i in range(qtde_valores):
        for j in range(i, qtde_valores):
            for k in range(j, qtde_valores):
                if vec[i]+vec[j]+vec[k] == 0:
                    sum3.append([vec[i], vec[j], vec[k]])

    end = time.time_ns()
    return sum3, end - start


def sum3_bisect():
    start = time.time_ns()
    sum3 = []
    end = time.time_ns()
    return sum3, end - start


def sum3_optimized():
    start = time.time_ns()
    sum3 = []
    end = time.time_ns()
    return sum3, end - start


def main():
    # criação dos vetores de 100, 500, 1000, 2000 e 50000
    # 10 vetores para cada
    qtde_exec = 1
    random.seed(0)
    vetor_tamanhos = [100, 500, 1000, 2000, 5000]
    vetores_dados = []
    for i in range(len(vetor_tamanhos)):
        vetores_dados.append([])
        for k in range(qtde_exec):
            vetores_dados[i].append([random.randint(-1000, 1000)
                                     for j in range(vetor_tamanhos[i])])

    # execução dos algoritmos, armazenamento
    # dos dados de retorno e dos tempos de execução. Os dados
    # retornados serão comparados com as execuções dos outros algoritmos para
    # a verificação das execuções

    # Algoritmo 3-sum força bruta O(n³)
    print("Algoritmo 3-SUM Força bruta")
    vet_ret_fbruta = []
    vet_t_medio_fbruta = []
    for i in range(len(vetor_tamanhos)):
        vet_ret_fbruta.append([])
        t_medio = 0
        for j in range(qtde_exec):
            rv, t = sum3_fbruta(vetores_dados[i][j])
            vet_ret_fbruta[i].append(rv)
            t_medio += t
        # tempo médio em milisegundos
        t_medio /= qtde_exec
        # tempo médio em segundos
        t_medio /= 1000000000
        vet_t_medio_fbruta.append(t_medio)
        print("N:%d, T médio: %f" % (vetor_tamanhos[i], t_medio))
    print()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()
