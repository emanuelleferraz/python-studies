import sys
import os


def raizes(a, b, c):
    delta = (b ** 2 - 4 * a * c)
    x1 = (-b + delta**(1/2)) / (2 * a)
    x2 = (-b - delta**(1/2)) / (2 * a)
    
    print(f"\nO valor de X1 é igual a {x1:.2f}")
    print(f"O valor de X2 é igual a {x2:.2f}\n")
    
    # Retornar os valores em uma lista
    valores = []
    valores.append(x1)
    valores.append(x2)
    
    return valores
    
if __name__ == '__main__':
    while True:
        print("Calcular as raizes de uma equação de segundo grau")
        print("Equação no formato ax² + bx + c = 0\n")
        
        try:
            a = float(input("Entre com o valor de a: "))
            b = float(input("Entre com o valor de b: "))
            c = float(input("Entre com o valor de c: "))
        except ValueError:
            print("Digite somente números!")
        else:
            resultado = raizes(a, b, c)
            print(resultado)
            
        while True:
            continua = input("\nDigite q para sair ou n para novo cálculo: ")
            if (continua.lower() == 'q'):
                sys.exit()
            elif (continua.lower() == 'n'):
                os.system('cls')
                break
            else:
                print("Entrada inválida!")
    
    
    