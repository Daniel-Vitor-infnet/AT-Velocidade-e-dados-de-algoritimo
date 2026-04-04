import random
import sys

sys.setrecursionlimit(200000)  # evita erro em casos grandes


def gerar(n):
    return [random.randint(0, n//2) for _ in range(n)] # gerar duplicados


def remover_dup(arr):
    return list(set(arr))


# 🔹 Versão A (ordenando tudo):

def k_smallest_A(arr, k):
    return sorted(arr)[:k]


def partition(arr, l, r):
    # Escolhi o  pivô aleatório (evita pior caso)
    p = random.randint(l, r)
    arr[p], arr[r] = arr[r], arr[p]

    pivot = arr[r]
    i = l

    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


def quickselect(arr, l, r, k):
    while l <= r:
        p = partition(arr, l, r)

        if p == k:
            return
        elif p > k:
            r = p - 1
        else:
            l = p + 1


# 🔹 Versão B (QuickSelect)
def k_smallest_B(arr, k):
    a = arr.copy()
    quickselect(a, 0, len(a)-1, k)
    return a[:k]


# 🔹 Execução
tams = [1000, 10000, 25000, 50000, 100000]
k = 10

for n in tams:
    arr = gerar(n)
    arr = remover_dup(arr)

    print(f"\n== {n} ==")
    print("A:", k_smallest_A(arr, k))
    print("B:", k_smallest_B(arr, k))
    
# Primeiro removi os elementos duplicados do vetor utilizando um conjunto (set), simples rápido e efeiciente.
# Em seguida apliquei as duas versões da função (A e B) sobre o vetor sem duplicados, 
# garantindo que ambas usem os mesmos dados.