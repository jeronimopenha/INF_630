<h1> Exercício 1 - 12/09/2022</h1>

<table style:'border-style:none'>
    <tr>
        <td width="20%"><center><img src="./logo/brasao.png"></center></td>
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

<h2>Resolução</h2>

Para a resolução da atividade foram utilizados:
* Repositório do exercício: [Link.](https://github.com/jeronimopenha/INF_630)
* Um Desktop com o processador Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz e 16GB de memória RAM DDR3 1333MHz.
* Sistema Operacional Arch Linux com kernel 5.19.7-arch1-1 #1 SMP PREEMPT_DYNAMIC.
* Linguagem de programação python 3.10.6.
* Visual Studio Code versão 1.71.0.
* Função sort() para vetores em python que possui ordem de complexidade O(n log<sub>2</sub><sup>n</sup>)<sub>.[Ref](https://wiki.python.org/moin/TimeComplexity)</sub>
* Função bisect() para vetores em python que possui ordem de complexidade O(log<sub>2</sub><sup>n</sup>)<sub>.[Ref](https://docs.python.org/3/library/bisect.html#module-bisect)</sub>
* Os gráficos foram gerados com o auxílio da biblioteca Matplotlib.
* Utilização da biblioteca Time para a contagem do tempo de execução.
* Utilização da biblioteca Random para a geração de números aleatórios para os vetores de entrada.
* Execução para 10 listas aleatórias, porém iguais para cada experimento, com diferentes conteúdos e utilização do tempo médio das execuções.
* Utilização de valores grandes nas listas: Optou-se por valores de -10000 a +10000.
* Os códigos estão no arquivo sum3.py contido neste repositório.
* Para a instalação das dependências deste projeto: pip install --user -r  requirements.txt 
* Para a execução: python sum3.py
* Após a execução do script, o relatório será exibido no terminal com os tempos e valores de K<sub>(n)</sub> e salvo no arquivo relatorio.txt
* Os gráficos são salvos na pasta "graficos".
* Para este documento os gráficos e o relatório de execução estão disponíveis na pasta "relatorio".

<h3>Relatório de execução:</h3>

* Para estimar o tempo de execução para N=5000, foi acrescentada uma constante K<sub>médio</sub> multiplicada à equação de complexidade de cada algoritmo
* A constante K<sub>médio</sub> foi definida com a média das constantes K<sub>N</sub> calculadas para cada instância.
* O erro foi calculado pela equação do Erro Percentual: e = [(v_aprox - v)/v] * 100
    Onde:
    * **v_aprox:** é o valor aproximado encontrado
    * **v:** é o valor exato
    * **e:** é o erro
1. Algoritmo 3-SUM Força bruta

    **Execução:**

    |   N  | T<sub>(s)</sub> | K<sub>(n)<sub> |
    | ---- | --------------- | -------------- |
    

    * Onde K<sub>(n)</sub> =  T<sub>(n)</sub> / N<sup>3</sup>
    * K<sub>médio</sub> = ????????????????
    * T<sub>(n)<sub>(estimado)</sub></sub> = K * N<sup>3</sup>

    **Estimativa de tempos de execução e erros**
    |   N  | T<sub>(s)</sub> | T<sub>(e)<sub>(estimado)</sub></sub> | Erro<sub>(%)<sub> |
    | ---- | --------------- | ------------------------------------ |-------------- |
    

    * Para N = 5000, o valor estimado foi de ????????????????????

2. Algoritmo 3-SUM N<sup>2</sup>log<sub>2</sub><sup>n</sup>

    **Execução:**

    |   N  | T<sub>(s)</sub> | K<sub>(n)<sub> |
    | ---- | --------------- | -------------- |
    


    **Estimativa de tempos de execução e erros**
    |   N  | T<sub>(s)</sub> | T<sub>(e)<sub>(estimado)</sub></sub> | Erro<sub>(%)<sub> |
    | ---- | --------------- | ------------------------------------ |-------------- |
    

    * Para N = 5000, o valor estimado foi de ????????????????????

3. Algoritmo 3-SUM N<sup>2</sup>

    **Execução:**

    |   N  | T<sub>(s)</sub> | K<sub>(n)<sub> |
    | ---- | --------------- | -------------- |
    

    

    **Estimativa de tempos de execução e erros**
    |   N  | T<sub>(s)</sub> | T<sub>(e)<sub>(estimado)</sub></sub> | Erro<sub>(%)<sub> |
    | ---- | --------------- | ------------------------------------ |-------------- |
    

    * Para N = 5000, o valor estimado foi de ????????????????????

<h3>Gráficos de execução:</h3>


<h4>Gráficos para cada algoritmo com estimativa<h4>

<h3>Comentários sobre os resultados</h3>