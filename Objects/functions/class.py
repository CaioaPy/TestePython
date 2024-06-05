class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, movimento = False):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.movimento = movimento

    def __str__(self):
        return f"Bicileta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor} e movimento = {self.movimento}"

    def buzinar(self):
        print("*bibi*")
    
    def parar(self):
        movimento = False
        print("a bicicleta parou")

    def mover(self):
        movimento = True
        print("a bicicleta começou a se mover")

    
bicicleta1 = Bicicleta("azul", "nova", "2024", 1900)

bicicleta1.buzinar()

print(bicicleta1)