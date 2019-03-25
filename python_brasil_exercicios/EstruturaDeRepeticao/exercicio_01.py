nota = int(input("Digite uma nota de 0/10: "))

while nota < 0 or nota > 10:
    print("Valor invalido, tente novamente.")
    nota = int(input("Digite uma nota de 0/10: "))

print("Muito obrigado.")
