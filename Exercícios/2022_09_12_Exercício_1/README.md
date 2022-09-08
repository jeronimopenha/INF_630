# Exercício 1 - 12/09/2022

<table style:'border-style:none'>
    <tr>
        <td width="20%"><center><img src="./brasao.png"></center></td>
        <td width="50%">
            UFV - Universidade Federal de Viçosa<br>
            DPI - Departamento de Informática<br>
            Prof. André Gustavo dos Santos<br>
            INF 630 - Projeto e Análise Algoritmos - 2022/1
        </td>
        <td>
            Atividade 1<br>
            Para segunda 12/09/2022
            <br><br>
            Jeronimo Costa Penha - ES 91669
        </td>
    </tr>
</table>
<center><strong>Algoritmos para 3-SUM</strong></center>

O problema 3-Sum consiste em, dado uma lista de *n* números, decidir se existem 3 deles cuja soma seja 0. Na versão desta atividade, considere que deve descobrir todos os conjuntos de 3 com essa propriedade.

1. Algoritmo força-bruta:
    * Implementar o algoritmo força-bruta O(n<sup>3</sup>) comentado na aula
    * Anotar o tempo de execução para diferentes n (ex: 100, 500, 1000, 2000, 5000)
    * Estimar uma função de tempo em função de n: T (n) = ?
    * Verificar se a função de tempo é uma boa estimativa para n maiores (ex: 10000)
2. Comparação de algoritmos
    * Implementar o algoritmo O(n<sup>2</sup> log<sub>2</sub> <sup>n</sup>) com busca binária comentado na aula 
    * Implementar um algoritmo O(n<sup>2</sup>) (pesquise!)
    * Anotar o tempo de execução dos três algoritmos para diferentes n
    * Fazer gráfico comparativo dos tempos dos 3 algoritmos
    * Estimar ou verificar até que valor de n cada algoritmo resolve em 10 segundos

Obs.: não é necessário fazer análise teórica ou estatı́stica dos resultados, trata-se apenas de experimento.

###Resolução

Para a resolução da atividade foram utilizados:
* Um notebook com o processador Pentium(R) Dual-Core CPU T4500 @2.30GHz e 6GB de memória RAM DDR3 1333MHz.
* Sistema Operacional Arch Linux com kernel 5.19.7-arch1-1 #1 SMP PREEMPT_DYNAMIC
* Linguagem de programação python 3.10.6
* Visual Studio Code versão 1.71.0
* Função sort() para vetores em python que possui ordem de 
complexidade O(n log<sub>2</sub><sup>n</sup>)<sub>[Ref](https://wiki.python.org/moin/TimeComplexity)</sub>
* Função bisect() para vetores em python que possui ordem de complexidade O(log<sub>2</sub><sup>n</sup>)<sub>[Ref](https://docs.python.org/3/library/bisect.html#module-bisect)</sub>
* Utilização da biblioteca Matplotlib para a geração dos gráficos
* Utilização da biblioteca Time para a contagem do tempo de execução
* Execução para 10 várias listas aleatórias, porém iguais para cada experimento, com diferentes conteúdos e utilização do tempo médio das execuções
* Utilização de valores grandes nas listas: Optou-se por valores de -10000 a +10000.
* Os códigos estão no arquivo sum3.py contido neste repositório
* Para a execução, basta executar o comando: python sum3.py
* Após a execução do script, o relatório será exibido no terminal e os gráficos exibidos em janelas através do matplotlib

####Relatório de execução:

####Gráficos:

####Comentários sobre os resultados