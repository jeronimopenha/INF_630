from math import *

# Retora o índice de chave em vec se estiver presente, senão -1


def busca_binaria(vec: list, l: int, h: int, chave: int, times: int):
    #somente para inserir breakpoint para depuração de cada chave
    if chave == 1:
        a=1
    # Caso base
    if h >= l:
        m = (h + l) // 2
        # Se a chave está presente na posição m, então é ele mesmo
        if vec[m] == chave:
            times += 1
            return chave, m, times

        # Se a chave é menor que o conteúdo da posição m, então só pode estar às esquerda de m
        elif vec[m] > chave:
            times += 1
            return busca_binaria(vec, l, m - 1, chave, times)
        # Senão, a chave só poderá estar presente à direita de m
        else:
            times += 1
            return busca_binaria(vec, m + 1, h, chave, times)
    else:
        # A chave não foi encontrada no vetor
        return chave, -1, times


# Vetor de testes
vec = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]
chaves = vec.copy()
chaves.append(1)

# teste
for c in chaves:
    print(busca_binaria(vec, 0, len(vec)-1, c, 0))
