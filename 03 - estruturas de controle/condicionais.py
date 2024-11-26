# Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0
faltas = 0

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
faltas = int(input('Entre com a quantidade de faltas: '))

# Calcular a média aritmética das notas
media = (n1 + n2) / 2

if (faltas >= 10):
    print('Aluno reprovado por faltas.')
elif (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif (media >= 5):
    print('Você está de recuperação')
else:
    print('Aluno reprovado...')

print('Sua média é {}'.format(media))
