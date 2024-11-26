# Diferença em relação as listas: as estruturas são imutáveis

halogenios = ('F', 'CL', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
print(elementos)
# print(halogenios)
# print(len(halogenios))
# print(halogenios[3])

tupla = (5, 4, 3, 1, 4, 5, 7, 8, 1, 9, 10, 11, 3, 1, 5, 12, 13, 4)
print(tupla.count(1))
print('CL' in halogenios)
print(max(tupla))
print(min(tupla))

# Operações não disponíveis: append(), sort(), pop(), reverse().....

# for elemento in elementos:
#     print(f"Elemento químico: {elemento}")

# Criar lista através de uma tupla:
grupo17 = list(halogenios)
grupo17[0] = 'H'
print(grupo17)

# Criar tupla através de lista:
grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)

print(sorted(alcalinos))