# Fibonacci - Soma dos números anteriores
# 0, 1, 1, 2, 3, 5, 8, 13......

def fibonacci(numero):
    if numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]
    else:
        sequenciaFibonacci = fibonacci(numero - 1)
        sequenciaFibonacci.append(sequenciaFibonacci[-1] + sequenciaFibonacci[-2])
        return sequenciaFibonacci
    
if __name__ == '__main__':
    
    try:
        numero = int(input("Digite um numero para calcular a sequência de fibonacci: "))
        resultado = fibonacci(numero)
    except RecursionError:
        print("Número inválido! Forneça apenas números inteiros positivos.")
    else:
        print(f"A sequencia de Fibonacci é {resultado}")
        
        