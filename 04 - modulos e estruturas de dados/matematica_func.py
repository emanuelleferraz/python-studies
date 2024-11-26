# Funções built-in e módulo math
import math

a = -5
b = 4
c = 2.78953
valores = [2, 5, 8, -1, 0, 11, 7, -6]

print(max(valores)) # -> maior valor
print(min(valores)) # -> menor valor
print(abs(a)) # -> valor absoluto
print(pow(a, b)) # -> exponenciação
print(round(c, 3)) # -> valor / casas decimais

# usando math
x = 8
y = 100

raiz_quadrada = math.sqrt(x)
print(math.ceil(raiz_quadrada)) # ceil - arrendonda o valor para o inteiro mais próximo

logaritmo = math.log10(y)
print(logaritmo)

print(math.pi) # -> valor de PI

print(math.factorial(x))
print(x / math.inf)