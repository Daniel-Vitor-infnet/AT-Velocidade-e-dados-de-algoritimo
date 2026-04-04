class Node:
    def __init__(self, v):
        self.v = v
        self.prev: "Node | None" = None
        self.next: "Node | None" = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # Inserções e Deleções: Tudo O(1)
    def insert_first(self, v):
        n = Node(v)
        if self.is_empty():
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        self.size += 1

    def insert_last(self, v):
        n = Node(v)
        if self.is_empty():
            self.head = self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            return print("Lista vazia")
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1

    def delete_last(self):
        if self.is_empty():
            return print("Lista vazia")
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1


class Deque:
    def __init__(self):
        self.lista = DoublyLinkedList()

    def insert_left(self, v): self.lista.insert_first(v)
    def insert_right(self, v): self.lista.insert_last(v)
    def remove_left(self): self.lista.delete_first()
    def remove_right(self): self.lista.delete_last()

    def peek_left(self):
        return self.lista.head.v if self.lista.head else None

    def peek_right(self):
        return self.lista.tail.v if self.lista.tail else None

    # Verifica se os ponteiros
    def verificar_invariantes(self):
        l = self.lista
        if l.is_empty():
            return l.head is None and l.tail is None
        check = (l.head.prev is None) and (l.tail.next is None)
        return check and (l.size > 0)


# --- Testes ---
d = Deque()
print("Invariante inicial:", d.verificar_invariantes())

d.insert_left(10) 
d.insert_right(20)
d.insert_left(5)
print(
    f"Esquerda: {d.peek_left()}, Direita: {d.peek_right()} | Invariante: {d.verificar_invariantes()}")

# Remoções
d.remove_left()    
d.remove_right()    
print(
    f"Esquerda: {d.peek_left()}, Direita: {d.peek_right()} | Tamanho: {d.lista.size}")
print("Invariante final:", d.verificar_invariantes())

# --- Complexidade e Analise (Questao 7) ---
"""
Complexidade por operacao:
- Todas as operacoes (insert_left/right, remove_left/right, peek) sao O(1).
- Isso acontece porque temos ponteiros diretos para o Head e para o Tail cada no sabe quem e o seu Anterior (prev) e Proximo (next).

Invariantes Estruturais:
- O tamanho (size) e atualizado em cada operção.
- Os ponteiros de extremidade sao limpos (None) quando a lista esvazia.
- A integridade e mantida pois Head.prev e Tail.next sempre apontam para None.
"""
