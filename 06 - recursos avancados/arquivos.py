# Manipulação de arquivos de texto.

# ** Leitura **

# print(f"Método read():\n")
# print(manipulador.read())

# print(f"Método read():\n")
# print(manipulador.readline())

# print(f"Método read():\n")
# print(manipulador.readlines()) #lista

# texto = input("Qual termo deseja procurar no arquivo? ")

# try:
#     manipulador = open("arquivo.txt", "r", encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print("A string foi encontrada!")
#             print(linha)
#         else:
#             print("String não encontrada!")
# except IOError:
#     print("Não foi possível abrir o arquivo.")
# else:
#     manipulador.close()


# ** Escrita **
# texto = "\nPython é usado em Ciência de Dados extensivamente."

# try:
#     manipulador = open("arquivo.txt", "a", encoding='utf-8') # w -> conteúdo será substituído / a -> conteúdo será acrescentado
#     manipulador.write(texto)

# except IOError:
#     print("Não foi possível abrir o arquivo.")
# else:
#     manipulador.close()

# ** WriteLineS **
frutas = ['Morango\n', 'Uva\n', 'Amora\n', 'Framboesa\n']

try:
    manipulador = open("frutas.dat", "w", encoding='utf-8') 
    manipulador.writelines(frutas)
except IOError:
    print("Não foi possível abrir o arquivo.")
else:
    manipulador.close()
    
# Lendo arquivo criado
try:
    manipulador = open("frutas.dat", "r", encoding='utf-8')
    print(manipulador.read())
except IOError:
    print("Não foi possível abrir o arquivo.")
else:
    manipulador.close()