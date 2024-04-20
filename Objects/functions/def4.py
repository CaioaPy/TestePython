x = input("x= ?")
y = input("y= ?")


def quadrado(num):
    num = float(num) * float(num)
    print(num)

decision = input("x or y")
decision.lower
if decision == "x":
    quadrado(x)
else:
    quadrado(y)