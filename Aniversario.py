print("Em que mês estamos? (apenas números)")
matual = int(input())
mesA = matual * 30

print("Que dia é hoje? (apenas números)")
datual = int(input())
total = mesA + datual

print("Qual o mês em que você faz aniversário? (apenas números)")
mdepois = int(input())
mesB = mdepois * 30

print("Qual o dia exato do seu aniversário? (apenas números)")
ddepois = int(input())
total2 = mesB + ddepois

ultima = total2 - total
print("Faltam", ultima, "dias para o seu aniversário!")
