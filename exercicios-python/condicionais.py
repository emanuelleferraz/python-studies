nota1 = nota2 = 0
mediaNotas = 0
numFaltas = 0

nota1 = float(input("Informe o valor da primeira nota: "))
nota2 = float(input("Informe o valor da segunda nota: "))

numFaltas = int(input("Informe o número de faltas: "))

mediaNotas = (nota1 + nota2) / 2

if (numFaltas > 18):
    print("Reprovado por faltas")
elif (mediaNotas >= 7):
    print("Aprovado!")
elif (mediaNotas >= 5):
    print("Recuperação")
else:
    print("Reprovado!")

print(f"Sua média é {mediaNotas}")