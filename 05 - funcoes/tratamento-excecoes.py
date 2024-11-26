# Exceções são objetos que representa um erro que ocorreu ao executar um programa.
# Blocos try ... except (ZeroDivisionError, ValueError)

def divisao(a, b):
    return round(a / b, 2)

if __name__ == '__main__':
    while True:
        try:
            num1 = int(input("Digite um número: "))
            num2 = int(input("Digite um outro número: "))
            break
        except ValueError:
            print(f"Ocorreu um erro ao ler o valor. Tente novamente.")
    try:
        resultado = divisao(num1, num2)
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
    except:
        print("Ocorreu um erro desconhecido.")     
    else:
        print(f"Resultado: {resultado}")  
    finally:
        print(f"\nFim do cálculo.")