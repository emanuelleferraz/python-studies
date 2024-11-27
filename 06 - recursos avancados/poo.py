# Orientação a objetos: Paradigma de Programação
# Classes e Objetos

class Veiculo:
    def movimentar(self):
        print("Sou um veículo e me desloco!")
        
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante #encapsulamento usando underscore
        self.__modelo = modelo
        self.__numRegistro = None
        
    # Setter
    def setNumeroRegistro(self, registro):
        self.__numRegistro = registro
        
    # Getter
    def getFabricanteModelo(self):
        print(f"Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n")
        
    def getNumeroRegistro(self):
        return self.__numRegistro
    
    
class Carro(Veiculo):
    # Método __init__ será herdado
    def movimentar(self):
        print("Sou um carro e ando pelas ruas!") #Polimorfismo

class Motocicleta(Veiculo):
    def movimentar(self):
        print("Corro muito!")
        
class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__categoria = categoria
        super().__init__(fabricante, modelo) #superclasse - a classe da qual avião herda
    
    def getCategoria(self):
        return self.__categoria
    
    def movimentar(self):
        print("Eu voo alto!")
    
if __name__ == '__main__':
    # meuVeiculo = Veiculo("GM", "Cadillac Escalade")
    # meuVeiculo.movimentar()
    # meuVeiculo.getFabricanteModelo()
    # meuVeiculo.setNumeroRegistro("499244-1")
    # print(f"Registro: {meuVeiculo.getNumeroRegistro()}\n")
    
    
    # meuCarro = Carro("Volkswagen", "Polo")
    # meuCarro.movimentar()
    # meuCarro.getFabricanteModelo()
    
    # seuCarro = Carro("Audi", "A5 Sportback")
    # seuCarro.movimentar()
    # seuCarro.getFabricanteModelo()
    
    # moto = Motocicleta("Harley-Davidson", "Nightster Special")
    # moto.movimentar()
    # moto.getFabricanteModelo()
    
    meuAviao = Aviao("Boeing", "747", "Comercial")
    meuAviao.movimentar()
    meuAviao.getFabricanteModelo()
    print(f"Categoria: {meuAviao.getCategoria()}")