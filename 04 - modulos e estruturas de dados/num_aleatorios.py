import random

# print("Gerar cinco números aleatórios entre 1 e 50: \n")
# for i in range(5):
#     numero = random.randint(1,50)
#     print(f"Número gerado: {numero}")

# valor = random.random() -> *gera float*
# print(f"Número gerado: {round(valor * 10, 2)}")

# valor = random.uniform(1, 100) -> *outra forma de gerar float*
# print(f"Número: {round(valor, 2)}")

lista = [2, 4, 6, 9, 10, 13, 14, 16, 18, 20, 21, 27, 33]
# numero = random.choice(lista) -> *escolher um num aleatório da lista*

# print(f"Número escolhido: {numero}")

# numero = random.sample(lista, 3) -> escolher mais de um num da lista
# print(f"Números escolhidos: {numero}")

print(f"Lista original: {lista}")
print(f"Exibindo a lista embaralhada: ")
numero = random.shuffle(lista)
print(lista)