# Trocar valores entre duas variáveis

var1 = 12
var2 = 31

# var2, var1 = var1, var2

# print(f'var1: {var1}, var2: {var2}')

# Operador Condicional Ternário
# menor = var1 if var1 < var2 else var2
# print(f'Menor valor: {menor}')
# print(f'Menor valor: {(var2, var1)[var1 < var2]}')

# Generators

# valores = [1,3,5,7,9,11,13,15]
# quadrados = (item**2 for item in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)

# Função enumerate()
# bebidas = ['Café', 'Chá', 'Água', 'Suco', 'Refrigerante']
# for i, item in enumerate(bebidas):
#     print(f'Índice: {i}, Item: {item}')

# temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
# total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f'A temperatura em {i} é negativa, com {t}°C.')

# Gerenciamento de contexto com with

try:
    a = open('frutas.dat','r', encoding='utf-8')
    print(a.read())
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    a.close()

with open('frutas.dat','r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end='')
    
