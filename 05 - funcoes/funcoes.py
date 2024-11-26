# Função com argumentos

# def soma(a, b):
#     return a + b

# print(soma(12, 7))

# def multiplicacao(a, b):
#     return a * b

# a = 10
# b = 10

# c = multiplicacao(a, b)
# print(c)

# def divisao(a, b):
#     if (b != 0):
#         return a / b
#     else:
#         return "Não é possível dividir por zero."

# if __name__ == '__main__':
#     a = int(input("Informe um número: "))
#     b = int(input("Informe outro número: "))
    
#     resultado = divisao(a, b)
#     print(f"{a} dividido por {b} é igual a {resultado}")

# Exemplo com uma função recebendo mais de um valor
def quadrado(valor):
    quadrados = []
    for numero in valor:
        quadrados.append(numero ** 2)
    return quadrados

if __name__ == "__main__":
    valores = [2, 4, 6, 8, 10]
    resultado = quadrado(valores)
    
    for valor in resultado:
        print(valor)
    