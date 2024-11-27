# Funções Lambda (anônimas) -> não tem nome, podem ser criadas e usadas no mesmo momento
# Sintaxe:
# lambda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(1, 11):
#     print(quadrado(i))

# par = lambda x: x % 2 == 0
# print(par(8)) #True ou False

funcao_celsius = lambda fah: (fah - 32) * 5/9
print(funcao_celsius(82))


# Função map():
# Sintaxe: map(função, iterável)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
dobro = list(map(lambda x: x * 2, numeros))
print(dobro)

palavras = ["Python", "é", "divertido"]
maiusculas = list(map(str.upper, palavras))
print(maiusculas)


# Função filter():
# Sintaxe: filter(função, sequência)

def numeros_pares(num):
    return num % 2 == 0

numerosLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
num_par = list(filter(numeros_pares, numerosLista))
print(num_par)


# Função reduce():
# Sintaxe: reduce(função, sequência, valor_inicial)

from functools import reduce

# def multiplica(a, b):
#     return a * b

# listaNumeros = [1, 2, 3, 4, 5, 6]

# total = reduce(multiplica, listaNumeros)
# print(total)

# Exemplo com soma cumulativa dos quadrados de valores usando lambda
listaNumeros = [1, 2, 3, 4]

total = reduce(lambda x, y: x**2 + y**2, listaNumeros)
print(total)
