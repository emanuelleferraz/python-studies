# Manipulando Arquivos CSV

import csv

# Gerênciamento de contexto usando um alias 'as ...'
# with open("elementos.csv", mode='r', encoding='utf-8') as arq: 
#     leitor = csv.reader(arq, delimiter=',')
#     cont = 0
#     for linha in leitor:
#         if cont == 0:
#             print(f"Colunas: {" ".join(linha)}\n")
#             cont+=1
#         else:
#             print(f"Elemento {linha[0]} é o {linha[1]}.")
#             cont+=1
#     print(f"Foram lidas {cont} linhas.")

# De outra forma..
# simbolos = []

# with open("elementos.csv", mode='r', encoding='utf-8') as arq: 
#     leitor = csv.reader(arq, delimiter=',')
#     for indice, linha in enumerate(leitor): #função que retorna os dados enumerando o indice de cada linha
#         if indice == 0:
#             pass
#         else:
#             simbolos.append(linha[2])
#     print(simbolos)

# ** Escrita ** - Adicionar mais conteúdo

with open("elementos.csv", mode='a', encoding='utf-8', newline='') as arq:
    escritor = csv.writer(arq, delimiter=',')
    escritor.writerow(['7', 'Nitrogênio', 'N', '15'])
    escritor.writerow(['8', 'Oxigênio', 'O', '16'])
    escritor.writerow(['9', 'Fluor', 'F', '17'])
