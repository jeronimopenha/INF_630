import random
import time
import traceback
import matplotlib.pyplot as plt
import bisect
from math import log2


def calc_k_f_b(t_medio, n):
    return t_medio/pow(n, 3)


def calc_k_b_b(t_medio, n):
    # nlog2n * n2 log2n
    # return t_medio/(n*log2(n)*pow(n, 2)*log2(n))
    return t_medio/(pow(n, 2)*log2(n))


def calc_k_o(t_medio, n):
    return t_medio/pow(n, 2)


def calc_t_est_f_b(k_medio, n):
    return k_medio * pow(n, 3)


def calc_t_est_b_b(k_medio, n):
    # return k_medio * n*log2(n)*pow(n, 2)*log2(n)
    return k_medio * pow(n, 2)*log2(n)


def calc_t_est_o(k_medio, n):
    return k_medio * pow(n, 2)


def sum3_fbruta(vec_):
    vec = vec_.copy()
    vec.sort()
    start = time.time_ns()
    sum3 = []
    qtde_valores = len(vec)
    for i in range(qtde_valores):
        for j in range(i+1, qtde_valores):
            for k in range(j+1, qtde_valores):
                if vec[i]+vec[j]+vec[k] == 0:
                    sum3.append([vec[i], vec[j], vec[k]])
                    break

    end = time.time_ns()
    return sum3, end - start


def sum3_bisect(vec_):
    vec = vec_.copy()
    vec.sort()
    start = time.time_ns()
    sum3 = []
    qtde_valores = len(vec)
    for i in range(qtde_valores):
        for j in range(i+1, qtde_valores):
            l = (vec[i] + vec[j]) * -1
            k = bisect.bisect_left(vec[j+1:qtde_valores], l)
            if (k + j + 1) != qtde_valores and vec[(k + j + 1)] == l:
                sum3.append([vec[i], vec[j], vec[k]])

    end = time.time_ns()
    return sum3, end - start


def sum3_optimized(vec_):
    vec = vec_.copy()
    vec.sort()
    start = time.time_ns()
    sum3 = []
    qtde_valores = len(vec)
    for i in range(qtde_valores):
        j = i+1
        k = qtde_valores - 1
        while (j < k):
            s = vec[i] + vec[j] + vec[k]
            if s > 0:
                k -= 1
            elif s < 0:
                j += 1
            else:
                sum3.append([vec[i], vec[j], vec[k]])
                j += 1
    end = time.time_ns()
    return sum3, end - start


def salva_grafico(titulo, label_x, label_y, vetor_x, vetores_y, nome_arquivo):
    # gráfico para os tempo de execução do algoritmo com os tempos estimados
    plt.clf()
    plt.title("%s" % titulo)
    plt.xlabel("%s" % label_x)
    plt.ylabel("%s" % label_y)
    plt.grid(False)
    for i in vetores_y:
        plt.plot(vetor_x, i[0], label=i[1], lw=3, ls=i[2])
    plt.legend()
    plt.savefig("./graficos/%s.png" % nome_arquivo)


def exec_experimento(funcao, eq_k, eq_t, nome_exp, nome_arquivo, vetor_tamanhos, vetores_dados, qtde_exec, qtde_exp):
    relatorio = "Algoritmo %s\n" % nome_exp
    vet_ret = []
    k_medio = 0
    vet_t_medio = []
    relatorio += "| N | T(s) | K(n) |\n"
    for i in range(qtde_exp):
        vet_ret.append([])
        t_medio = 0
        for j in range(qtde_exec):
            rv, t = funcao(vetores_dados[i][j])
            vet_ret[i].append(rv)
            t_medio += t
        # tempo médio em milisegundos
        t_medio /= qtde_exec
        # tempo médio em segundos
        t_medio /= 1000000000
        n = vetor_tamanhos[i]
        k = eq_k(t_medio, n)
        k_medio += k
        vet_t_medio.append(t_medio)
        relatorio += "| %d | %.3f | %.3e |\n" % (n, t_medio, k)
    k_medio /= (qtde_exp)
    relatorio += "\n"

    relatorio += "Estimativa de tempos\n"
    vet_t_est = []
    relatorio += "| N | K(medio) | T(s) | T(s)(estimado) | Erro(%) |\n"
    for i in range(qtde_exp):
        n = vetor_tamanhos[i]
        t_est = eq_t(k_medio, n)
        vet_t_est.append(t_est)
        erro = (t_est - vet_t_medio[i])/vet_t_medio[i] * 100
        relatorio += "| %d | %.3e | %.3f | %.3f | %.3f |\n" % (
            n, k_medio, vet_t_medio[i], t_est, erro)
    relatorio += "\n"

    with open('./retorno/%s.txt' % nome_arquivo, 'w') as f:
        f.write(relatorio)
        f.close()

    vet_grafico = [[vet_t_medio, "T_exec", "-"], [vet_t_est, "T_est.", "--"]]
    salva_grafico(nome_exp, "N", "Segundos",
                  vetor_tamanhos, vet_grafico, nome_arquivo)
    print(relatorio)
    return vet_t_medio, vet_t_est, k_medio, vet_ret


def main():
    # criação dos vetores de 100, 500, 1000, 2000 e 50000
    # 10 vetores para cada
    qtde_exec = 10
    random.seed(0)
    vetor_tamanhos = [100, 500, 1000, 2000, 5000]
    qtde_exp = len(vetor_tamanhos)
    vetores_dados = []
    for i in range(qtde_exp):
        vetores_dados.append([])
        for k in range(qtde_exec):
            vetores_dados[i].append([random.randint(-1000, 1000)
                                    for j in range(vetor_tamanhos[i])])

    # Algoritmo 3-sum com busca binária O(n² log2 n)
    bb_t_medio, bb_t_est, bb_k, bb_vet_ret = exec_experimento(
        sum3_bisect, calc_k_b_b, calc_t_est_b_b,
        "3-SUM Busca Binária", "sum_3_b_b",
        vetor_tamanhos, vetores_dados, qtde_exec, qtde_exp)
    '''with open('./relatorio/sum_3_bb_data.txt', 'w') as f:
        f.write(bb_t_medio)
        f.write(bb_t_est)
        f.write(bb_k)
        f.write(bb_vet_ret)
        f.close()'''

    # Algoritmo 3-sum otimizado O(n²)
    o_t_medio, o_t_est, o_k, o_vet_ret = exec_experimento(
        sum3_optimized, calc_k_o, calc_t_est_o,
        "3-SUM Otimizado", "sum_3_o",
        vetor_tamanhos, vetores_dados, qtde_exec, qtde_exp)

    # Algoritmo 3-sum força bruta O(n³)
    bf_t_medio, bf_t_est, bf_k, bf_vet_ret = exec_experimento(
        sum3_fbruta, calc_k_f_b, calc_t_est_f_b,
        "3-SUM Força Bruta", "sum_3_f_b",
        vetor_tamanhos, vetores_dados, qtde_exec, qtde_exp)
    print("Estimativa para N = 10000: %.3f\n" % (calc_t_est_f_b(bf_k, 10000)))

    vet_grafico = [
        [bf_t_medio, "T_fb.", "-"],
        [bb_t_medio, "T_bb", "--"],
        [o_t_medio, "T_otm.", "-."]
        ]
    salva_grafico("Experimentos", "N", "Segundos",
                  vetor_tamanhos, vet_grafico, "exp")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()
