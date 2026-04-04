# Questão é "a, b, c" e novamente "a e b". Vou transforma o "a" em d e o "b" em e, para não confundir com as outras questões.

import random

# Questão 1.a:

def linear_search(arr, target):
    comparacoes = 0
    for i, valor in enumerate(arr):
        comparacoes += 1
        if valor == target:
            return i, comparacoes
    return -1, comparacoes

# d (Proponha uma estratégia de “falha rápida”):
def is_sorted_fast(arr, k=10):
    """
    Estratégia de amostragem aleatória O(1).
    Verifica as extremidades e k pares aleatórios.
    """
    n = len(arr)
    if n <= 1: return True
    if arr[0] > arr[-1]: return False # Falha rápida básica
    
    for _ in range(k):
        i = random.randint(0, n - 2)
        if arr[i] > arr[i + 1]:
            return False
    return True

def binary_search(arr, target):
    # Etapa explícita de verificação de pré condição (array ordenado)
    if not is_sorted_fast(arr):
        return -1, 0, "ERRO: vetor não ordenado"

    baixo = 0
    alto = len(arr) - 1
    comparacoes = 0

    while baixo <= alto:
        comparacoes += 1
        meio = (baixo + alto) // 2

        if arr[meio] == target:
            return meio, comparacoes, None
        elif arr[meio] < target:
            baixo = meio + 1
        else:
            alto = meio - 1

    return -1, comparacoes, None

# b (Crie um gerador de vetores de tamanho n):
def gerar_vetor(n, ordenado=False):
    arr = random.sample(range(1, n*3), n)
    if ordenado:
        arr.sort()
    return arr

# c (Execute para n em pelo menos 5 escalas e registre as contagens):
tamanhos = [500, 5000, 50000, 500000, 5000000] # Volores simples para teste, podem ser ajustados para escalas maiores.

print(f"{'n':>10} | {'Linear Comps':>15} | {'Binária Comps':>15}")
print("-" * 45)


for n in tamanhos:
    # Para o teste, um vetor e o ordenamos para a busca binária
    arr_base = gerar_vetor(n)
    alvo = arr_base[-1] # Testando pior caso (último elemento)

    _, comp_lin = linear_search(arr_base, alvo)

    arr_ord = sorted(arr_base)
    _, comp_bin, erro = binary_search(arr_ord, alvo)

    print(f"{n:10d} | {comp_lin:15d} | {comp_bin:15d}")

# e (Justificativa):
"""
Justificativa da estratégia (Questão 1.e):

1. Sobre o Big O: 
   - Se eu fosse checar o vetor todo ia ser O(n), dai a busca binaria ia fica lerda e perder o sentido de ser O(log n).
   - Com a amostragem a gente faz só umas 10 checagem (k constante) entao é O(1). 
   - É muito mais rapido q mandar ordenar tudo denovo com O(n log n).

2. Sobre o risco de dar ruim (falso positivo):
   - Tem o risco do algoritmo achar q ta ordenado sendo q nao ta, pq as amostra sorteada podem dar a sorte de estarem na ordem certa. 
   - É tipo um "trade-off": a gente abre mao de ter 100% de certeza pra ganhar uma velocidade absurda quando o vetor é gigante.
"""