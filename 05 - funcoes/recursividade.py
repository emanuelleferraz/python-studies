# Recursividade

# Fórmula geral para o FATORIAL:
# fatorial(numero) = 1, se o numero = 0 ou se o numero = 1 -> 'Caso Base'
# fatorial(numero) = numero * fatorial(numero - 1), para numeros > 1 -> 'Caso Recursivo'

def fatorial(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)
    
if __name__ == '__main__':
    numero = int(input("Digite um número inteiro para calcular o seu fatorial: "))
    try:
        resposta = fatorial(numero)
    except RecursionError:
        print("O número fornecido é muito grande ou negativo!")
    else:
        print(f"O fatorial de {numero} é igual a {resposta}")
