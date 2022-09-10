import random
import time
import traceback
import matplotlib.pyplot as plt
import bisect


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


def sum3_bisect(vec):
    start = time.time_ns()
    sum3 = []
    qtde_valores = len(vec)
    for i in range(qtde_valores):
        for j in range(i, qtde_valores):
            l = (vec[i] + vec[j]) * -1
            k = bisect.bisect_left(vec, l)
            if k != qtde_valores and vec[k] == l:
                sum3.append([vec[i], vec[j], vec[k]])

    end = time.time_ns()
    return sum3, end - start


def sum3_optimized(vec):
    start = time.time_ns()
    sum3 = []
    qtde_valores = len(vec)
    for i in range(qtde_valores):
        j = i+1
        k =  qtde_valores - 1
        while(j<k):
            if vec[i] + vec[j] + vec[k]  > 0:
                k-=1
            elif vec[i] + vec[j] + vec[k]  < 0:
                j+=1
            elif vec[i] + vec[j] + vec[k]  == 0:
                sum3.append([vec[i], vec[j], vec[k]])
    end = time.time_ns()
    return sum3, end - start


def salva_grafico(titulo, label_x, label_y, vetor_x, vetores_y, nome_arquivo):
    # gráfico para os tempo de execução do algoritmo com os tempos estimados
    plt.title("%s" % titulo)
    plt.xlabel("%s" % label_x)
    plt.ylabel("%s" % label_y)
    plt.grid(False)
    for i in vetores_y:
        plt.plot(vetor_x, vetores_y[0],
                 label=vetores_y[1], lw=3, ls=vetores_y[2])
    plt.legend()
    plt.savefig("./graficos/%s.png", nome_arquivo)


def exec_experimento(funcao, nome_exp, nome_arquivo, vetor_tamanhos, vetores_dados, qtde_exec, qtde_exp):
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
        k = t_medio/pow(n, 3)
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
        t_est = k_medio * pow(n, 3)
        vet_t_est.append(t_est)
        erro = (t_est - vet_t_medio[i])/vet_t_medio[i] * 100
        relatorio += "| %d | %.3e | %.3f | %.3f | %.3f |\n" % (
            n, k_medio, vet_t_medio[i], t_est, erro)
    relatorio += "\n"

    relatorio += "Estimativa para N = 5000: %.3f\n" % (k_medio * pow(5000, 3))
    with open('./relatorio/%s.txt' % nome_arquivo, 'w') as f:
        f.write(relatorio)
        f.close()

    vet_grafico = [[vet_t_medio, "T_exec", "-"], [vet_t_est, "T_est.", "--"]]
    salva_grafico(nome_exp, "N", "Segundos",
                  vetor_tamanhos, vet_grafico, nome_arquivo)


def main():
    # criação dos vetores de 100, 500, 1000, 2000 e 50000
    # 10 vetores para cada
    qtde_exec = 10
    random.seed(0)
    vetor_tamanhos = [100, 200]
    qtde_exp = len(vetor_tamanhos)
    vetores_dados = []
    for i in range(qtde_exp):
        vetores_dados.append([])
        for k in range(qtde_exec):
            vetores_dados[i].append([random.randint(-1000, 1000)
                                    for j in range(vetor_tamanhos[i])])
    # Algoritmo 3-sum força bruta O(n³)
    exec_experimento(sum3_fbruta, "3-SUM Força Bruta", "sum_3_f_b", vetor_tamanhos,
                     vetores_dados, qtde_exec, qtde_exp)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()
