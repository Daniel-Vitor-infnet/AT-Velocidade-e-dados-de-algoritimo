import random
import sys

# Essencial para não crashar o PC em listas ordenadas (Tive que pesquisar pq nada dava certo)
sys.setrecursionlimit(200000)

def gerar(n):
    b = list(range(n))
    q = b.copy()
    for _ in range(n//10):
        i, j = random.randint(0,n-1), random.randint(0,n-1)
        q[i], q[j] = q[j], q[i]
    return {"Ord": b, "Rev": b[::-1], "Qua": q, "Ale": random.sample(range(n*2), n)}

def bubble(arr):
    a = arr.copy(); c = m = 0
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            c += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                m += 3
    return c, m

def selection(arr):
    a = arr.copy(); c = m = 0
    n = len(a)
    for i in range(n):
        mi = i
        for j in range(i+1, n):
            c += 1
            if a[j] < a[mi]: mi = j
        if mi != i:
            a[i], a[mi] = a[mi], a[i]; m += 3
    return c, m

def insertion(arr):
    a = arr.copy(); c = m = 0
    for i in range(1, len(a)):
        k = a[i]; m += 1
        j = i-1
        while j >= 0 and a[j] > k:
            c += 1
            a[j+1] = a[j]; m += 1; j -= 1
        a[j+1] = k; m += 1
    return c, m

class No:
    def __init__(self, v): self.v=v; self.l=self.r=None

def ins(r, v, c):
    if not r: return No(v), c
    c += 1
    if v < r.v: r.l, c = ins(r.l, v, c)
    else: r.r, c = ins(r.r, v, c)
    return r, c

def walk(r, w):
    if not r: return w + 1
    w += 1
    w = walk(r.l, w)
    w = walk(r.r, w)
    return w

def bst(arr):
    r = None; c = 0
    for v in arr: r, c = ins(r, v, c)
    return c, walk(r, 0)

# Escalas do enunciado
tams = [1000, 10000, 25000, 50000, 100000]

for n in tams:
    print(f"\n--- N: {n} ---")
    dados = gerar(n)
    for nome, v in dados.items():
        # cospe o resultado direto
        res_b = bubble(v)
        res_s = selection(v)
        res_i = insertion(v)
        res_t = bst(v)
        print(f"{nome} -> Bub:{res_b} | Sel:{res_s} | Ins:{res_i} | BST:{res_t}")