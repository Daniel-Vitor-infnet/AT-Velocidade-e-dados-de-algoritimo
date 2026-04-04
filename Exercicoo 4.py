class HashTableChained:
    def __init__(self, cap=8):
        self.cap = cap
        self.size = 0
        self.buckets = [[] for _ in range(cap)]
        self.comps = 0 # contador de comparacoes

    def _hash(self, key):
        return hash(key) % self.cap


    def __len__(self):
        return self.size

    def _rehash(self):
        velhos = self.buckets
        self.cap *= 2
        self.buckets = [[] for _ in range(self.cap)]
        
        # Reinsere os itens sem disparar novo rehash
        for b in velhos:
            for k, v in b:
                idx = self._hash(k)
                self.buckets[idx].append((k, v))

    def put(self, key, value):
        # Limiar de 0.75 conforme pedido
        if self.size / self.cap > 0.75:
            self._rehash()

        idx = self._hash(key)
        b = self.buckets[idx]

        for i, (k, v) in enumerate(b):
            self.comps += 1
            if k == key:
                b[i] = (key, value) # atualiza valor
                return

        b.append((key, value))
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        b = self.buckets[idx]
        for k, v in b:
            self.comps += 1
            if k == key: return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        b = self.buckets[idx]
        for i, (k, v) in enumerate(b):
            self.comps += 1
            if k == key:
                del b[i]
                self.size -= 1
                return True
        return False

# --- Testes ---
ht = HashTableChained()
for i in range(50): ht.put(i, i*10)

ok = True
for i in range(50):
    if ht.get(i) != i*10: ok = False

print("Acessiveis apos rehash:", ok)
print("Capacidade final:", ht.cap)
print("Itens:", len(ht))
print("Comparacoes totais:", ht.comps)

# Relacao custo vs fator de carga (Questao 4 final)
"""
Custo esperado: O(1 + alpha), onde alpha é o fator de carga.
Como o rehash mantem o load factor < 0.75 as listas (buckets) 
ficam curta mantendo a busca muito rapida (quase constante).
"""