class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha, movimento = False):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha
        self.movimento = movimento

    #def __str__(self):
    #    return f"Bicileta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor} e movimento = {self.movimento}"
    
    #dict method
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

    def buzinar(self):
        print("*bibi*")
    
    def parar(self):
        movimento = False
        print("a bicicleta parou")

    def mover(self):
        movimento = True
        print("a bicicleta começou a se mover")

    def trocar_marcha(self, marcha2):
        if self.marcha < marcha2:
            print("trocando de marcha!")
            print(f"nova marcha: {marcha2}")
        else:
            print("nao é possivel trocar de marcha")

    
bicicleta1 = Bicicleta("azul", "nova", "2024", 1900, 2)

bicicleta1.buzinar()

print(bicicleta1)

bicicleta1.trocar_marcha(3)