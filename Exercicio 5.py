import random
from collections import deque

class Node:
    def __init__(self, v):
        self.v = v
        self.l = self.r = None

def inserir(raiz, v):
    if not raiz: return Node(v)
    atual = raiz
    while True:
        if v < atual.v:
            if not atual.l:
                atual.l = Node(v)
                break
            atual = atual.l
        else:
            if not atual.r:
                atual.r = Node(v)
                break
            atual = atual.r
    return raiz

def bfs(raiz):
    if not raiz: return [], 0
    # Fila (deque) conforme pedido
    fila = deque([raiz])
    res, passos = [], 0
    while fila:
        no = fila.popleft()
        passos += 1
        res.append(no.v)
        if no.l: fila.append(no.l)
        if no.r: fila.append(no.r)
    return res, passos

def dfs(raiz):
    if not raiz: return [], 0
    # Pilha (stack) conforme pedido
    pilha = [raiz]
    res, passos = [], 0
    while pilha:
        no = pilha.pop()
        passos += 1
        res.append(no.v)
        # Direita primeiro para processar Esquerda antes (estilo Pre-Order)
        if no.r: pilha.append(no.r)
        if no.l: pilha.append(no.l)
    return res, passos

# --- Teste ---
raiz = None
for _ in range(15): raiz = inserir(raiz, random.randint(1, 100))

res_b, p_b = bfs(raiz)
res_d, p_d = dfs(raiz)

print(f"BFS (Nivel): {res_b} | Passos: {p_b}")
print(f"DFS (Caminho): {res_d} | Passos: {p_d}")

# --- Analise Resumida ---
"""
1. Esforço (Big O): 
   - Os dois sao O(n) porque tem que passar por todos os nos da arvore de qualquer jeito.
   - O gasto de memoria depende do formato da arvore: BFS sofre em arvore "cheia" 
     e DFS sofre em arvore "comprida".

2. Pra que serve cada um:
   - BFS (Fila): Bom pra achar o caminho mais curto ou processar a arvore por "andares" (niveis).
   - DFS (Pilha): Bom pra explorar um caminho ate o fim (folhas) ou resolver labirintos.
"""