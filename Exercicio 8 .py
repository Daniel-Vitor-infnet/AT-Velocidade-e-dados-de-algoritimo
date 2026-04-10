'''
Bom o senhor comentou que poderia ter feito muito melhor e concordo. Fiquei com medo de tentar melhora as outras questões, 
porém fiquei com medo de tentar melhorar e acabar piorando kk. Então vou fazer apenas a questão 8 como o senhor pediu
Para o próximo AT vou me dedicar muito mais. Fiz o melhor que pude.
'''

'''
A memorização (memoization) evita desticamente a quantidade de chamadas recursivas, pois ele evita repetir os mesmo 
subproblemas já resolvidos.
Os subproblmeas distintos é ilimitado pela capacidade da mochila e número de itens.
Soluções recursivas complexidade exponencial O(2^n).
A versão com memoization reduz para O(nxW). Obs: O x é multiplicação
'''

class KnapsackRecursivo:
    def __init__(self):
        self.chamadas = 0
        self.subproblemas = set()

    def solve(self, valores, pesos, W):
        self.chamadas = 0
        self.subproblemas.clear()
        n = len(valores)
        resultado = self._knapsack(n - 1, W, valores, pesos)
        return resultado, self.chamadas, len(self.subproblemas)

    def _knapsack(self, i, capacidade, valores, pesos):
        self.chamadas += 1
        self.subproblemas.add((i, capacidade))

        if i < 0 or capacidade == 0:
            return 0

        if pesos[i] > capacidade:
            return self._knapsack(i - 1, capacidade, valores, pesos)

        sem_item = self._knapsack(i - 1, capacidade, valores, pesos)
        com_item = valores[i] + self._knapsack(i - 1, capacidade - pesos[i], valores, pesos)

        return max(sem_item, com_item)


class KnapsackMemo:
    def __init__(self):
        self.chamadas = 0
        self.memo = {}
        self.subproblemas = set()

    def solve(self, valores, pesos, W):
        self.chamadas = 0
        self.memo.clear()
        self.subproblemas.clear()
        n = len(valores)
        resultado = self._knapsack(n - 1, W, valores, pesos)
        return resultado, self.chamadas, len(self.subproblemas)

    def _knapsack(self, i, capacidade, valores, pesos):
        self.chamadas += 1
        chave = (i, capacidade)

        if chave in self.memo:
            return self.memo[chave]

        self.subproblemas.add(chave)

        if i < 0 or capacidade == 0:
            self.memo[chave] = 0
            return 0

        if pesos[i] > capacidade:
            resultado = self._knapsack(i - 1, capacidade, valores, pesos)
        else:
            sem_item = self._knapsack(i - 1, capacidade, valores, pesos)
            com_item = valores[i] + self._knapsack(i - 1, capacidade - pesos[i], valores, pesos)
            resultado = max(sem_item, com_item)

        self.memo[chave] = resultado
        return resultado




valores = [10, 55, 30, 50, 35, 40, 30, 45, 60, 20, 25, 55, 15, 45, 30, 50]
pesos  = [1, 4, 4, 5, 2, 3, 3, 5, 6, 2, 3, 7, 5, 4, 3, 5]
W = 20



k1 = KnapsackRecursivo()
r1, c1, s1 = k1.solve(valores, pesos, W)

print("=== Recursivo ===")
print("Valor máximo:", r1)
print("Chamadas:", c1)
print("Subproblemas:", s1)

k2 = KnapsackMemo()
r2, c2, s2 = k2.solve(valores, pesos, W)

print("\n=== Memorização (memoization) ===")
print("Valor máximo:", r2)
print("Chamadas:", c2)
print("Subproblemas:", s2)