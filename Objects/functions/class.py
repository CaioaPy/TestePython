class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, movimento = False):
        cor.self = cor
        modelo.self = modelo
        ano.self = ano
        valor.self = valor
        movimento.self = movimento

    def buzinar(self):
        print("*bibi*")
    
    def parar(self):
        movimento = False
        print("a bicicleta parou")
        
    def mover(self):
        movimento = True
        print("a bicicleta começou a se mover")
    