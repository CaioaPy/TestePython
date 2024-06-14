class Veiculo:
    def __init__(self, cor, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

class Carro(Veiculo):
    def __init__(self, cor, modelo, ano, carregado):
        super().__init__(cor, modelo, ano)
        self.carregado = carregado

    def Novacor(self, cor2):
        print(f"Cor alterada de {self.cor} para {cor2}")

class Bike(Veiculo):
    def __init__(self, cor, modelo, ano, rodas):
        super().__init__(cor, modelo, ano)
        self.rodas = rodas

carro = Carro("azul", "novo", 1942, False)

carro.Novacor("preto")