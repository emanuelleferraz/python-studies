import random

novoJogo = 'sim'

while novoJogo == 'sim':
    print("Seja bem vindo ao jogo de advinhação!")
    print("Objetivo do jogo: Acertar o número gerado entre 1 e 20")
    print("Regras: Você terá apenas três chances para adivinhar o número")

    numeroGerado = random.randint(1, 20)

    for i in range(3):
        print("\nEscolha um número: ")
        escolha = int(input())

        if(escolha == numeroGerado):
            print("\nParabens! Você acertou o número!")
            break
        elif(escolha > numeroGerado):
            print("Você escolheu um número maior.")
        else:
            print("Você escolheu um número menor.")

    if (escolha != numeroGerado):
        print(f"O número escolhido era: {numeroGerado}")

    novoJogo = input("Deseja jogar novamente? Digite 'sim' para iniciar um novo jogo ou 'não' para finalizar: ")
    novoJogo = novoJogo.lower()