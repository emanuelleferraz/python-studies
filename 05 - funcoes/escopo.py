# Escopo Global e Local


var_global = "Curso Completo de Python"

def escreve_texto():
    global var_global # Assim a variável global receberá o conteúdo declarado na função
    var_global = "Banco de Dados com SQL"
    var_local = "Fulano de Tal"
    print(f'Variável Global: {var_global}')
    print(f"Variável Local: {var_local}") # Só é possível acessar a variável local na função
    
if __name__ == '__main__':
    print(f"Executar a função escreve_texto()")
    escreve_texto()
    
    print("Tentar acessar as variáveis diretamente")
    print(f"Variável Global: {var_global}")
