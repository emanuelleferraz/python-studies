# Lista: representa uma sequência de valores

# Sintaxe: nome_lista = [valores]

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,11]
valores = n1 + n2

# print(sum(valores)) -> soma
# print(min(valores)) -> encontrar valor mínimo
# print(max(valores)) -> encontrar valor máximo

# valores.insert(3,21) -> posição a ser inserido / valor a ser inserido
# print(valores)
# print(17 in valores) -> existe o 17 na lista?

# planetas = ['Mercúrio', 'Vênus','Marte','Saturno','Urano','Netuno']
# for planeta in planetas:
#     print(planeta)


# **Outro exemplo:**

# adicionando elementos em uma lista:
# lista = []

# lista.append(1)
# lista.append("João Guilherme")
# lista.append([2, 3, 4])

# print(lista)

# # limpando lista:
# lista2 = [30, 40, 50]

# lista2.clear()
# print(lista2)

# # metodo copy:
# lista3 = [1, "Python", [40, 30, 20]]

# lista3.copy()
# print(lista3)

# # método count:
# listaCores = ["vermelho", "azul", "vermelho", "branco"]

# print(listaCores.count("vermelho"))
# print(listaCores.count("azul"))
# print(listaCores.count("branco"))

# # método extend:
# linguagens = ["python", "js", "ruby"]
# print(linguagens)

# linguagens.extend(["java", "csharp"]) # coloca tudo ao final da lista
# print(linguagens)

# # método pop:
# linguagens.pop() # remove o último inserido (conceito de pilha)
# print(linguagens)

# linguagens.pop(1) # remove pelo índice passado
# print(linguagens)

# # método remove:
# linguagens.remove("ruby") # remove pelo objeto
# print(linguagens)

# # método reverse:
# linguagens.append("csharp")
# linguagens.append("ruby")
# print(linguagens)

# linguagens.reverse()
# print(linguagens)

# # ordenando lista
# linguagens.sort()
# print(linguagens)

# linguagens.append("c")

# linguagens.sort(key=lambda x: len(x)) #ordena do menor para o maior
# print(linguagens)

# linguagens.sort(key=lambda x: len(x), reverse=True) #ordena do maior para o menor
# print(linguagens)

# # tamanho da lista
# print(len(linguagens))

# # sorted ou sort? diferença é que sorted é uma função
# print(sorted(linguagens, key=lambda x: len(x)))
# print(sorted(linguagens, key=lambda x: len(x), reverse=True))

bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita:')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas escolhidas:')
for bebida in bebidas:
    print(bebida)

print(f'\nSaúde!')
