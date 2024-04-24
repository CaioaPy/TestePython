tomada = True
monitor = True
computer_wires = True

def turn_on():
    if not tomada:
        print("a tomada não está ligada.")

    if not monitor:
        print("o monitor está desligado.")

    if not computer_wires:
        print("Os fios do computador não estão ligado corretamente.")
    
    else:
        print("Ligado!")