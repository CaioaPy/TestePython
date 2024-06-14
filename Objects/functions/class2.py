class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
    def Novacor(cor2):
        print(f"Cor alterada de {cor} para {cor2}")

carro = Carro("azul", "novo", 1942)

carro.Novacor("preto")