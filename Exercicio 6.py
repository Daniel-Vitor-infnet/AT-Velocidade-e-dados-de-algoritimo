class Node:
    def __init__(self, v):
        self.v = v
        self.next: 'Node | None' = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self): return self.size

    def __str__(self):
        if not self.head:
            return "Lista vazia"
        res, cur = [], self.head
        while cur:
            res.append(str(cur.v))
            cur = cur.next
        return " -> ".join(res)

    # O(1) - Insere direto no começo
    def insert_first(self, v):
        novo = Node(v)
        novo.next = self.head
        self.head = novo
        self.size += 1

    # O(n) - Tem que varrer a lista ate o fim
    def insert_last(self, v):
        if not self.head:
            return self.insert_first(v)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(v)
        self.size += 1

    # O(n) - Procura um valor e retorna a posicao
    def search(self, v):
        cur, p = self.head, 0
        while cur:
            if cur.v == v:
                return p
            cur, p = cur.next, p + 1
        return -1

    # O(n) - Remove por valor
    def delete(self, v):
        c, p = self.head, None
        while c:
            if c.v == v:
                if p:
                    p.next = c.next
                else:
                    self.head = c.next
                self.size -= 1
                return True
            p, c = c, c.next
        print(f"Erro: Valor {v} nao encontrado para delecao.")
        return False

    # O(n) - Insere em qualquer lugar (com validacao)
    def insert_at(self, i, v):
        if i < 0 or i > self.size:
            print(f"Erro: Indice {i} fora do limite (0-{self.size}).")
            return
        if i == 0:
            return self.insert_first(v)

        cur = self.head
        for _ in range(i - 1):
            cur = cur.next
        novo = Node(v)
        novo.next = cur.next
        cur.next = novo
        self.size += 1

    # O(n) - Deleta por indice (com validacao)
    def delete_at(self, i):
        if i < 0 or i >= self.size:
            print(f"Erro: Indice {i} invalido para lista de tam {self.size}.")
            return
        if i == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(i - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1


# --- Teste de Evidencia ---
l = SinglyLinkedList()
l.insert_first(10)
l.insert_last(30)
l.insert_at(1, 20)
print(f"Lista: {l}")
print(f"Busca 20: Posição {l.search(20)}")
l.delete(20)       # 10 -> 30
l.delete_at(0)     # 30
print(f"Final: {l} | Tamanho: {len(l)}")

# --- Analise de Custo (Questao 6) ---
"""
- insert_first: O(1) -> So mexe no ponteiro.
- insert_last:  O(n) -> Precisa do while pra achar o ultimo.
- search:       O(n) -> Pior caso percorre a lista toda.
- delete:       O(n) -> Precisa achar o indi
- insert_at:    O(n) -> Percorre ate o indice i-1.
- delete_at:    O(n) -> Percorre ate o indice i-1.
"""
