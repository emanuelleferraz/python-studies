# Comprimir lista: retorno, iteração, condição
# numeros = [1, 4, 7, 9, 10, 12, 21]

# quadrado = [num**2 for num in numeros] 
# print(quadrado)

# Criar uma lista de números pares de 0 a 10
# pares = [numero for numero in range(11) if numero % 2 == 0]
# print(pares)

# frase = "A lógica é apenas o princípio da sabedoria, não o seu fim."
# vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

# listaVogais = [vog for vog in frase if vog in vogais]
# print(f"A frase possui {len(listaVogais)} vogais: ")
# print(listaVogais)

#Distributiva entre valores de duas listas
distributiva = [k * m for k in [2, 3, 5] for m in [10, 20, 30]]
print(distributiva)