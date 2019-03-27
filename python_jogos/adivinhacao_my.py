#Biblioteca para gerar os numeros aleatórios
from random import randint

print("***********************************")
print("Bem vindo no jogo de Adivinhacação!")
print("***********************************")
print()

numero_secreto = randint(0,100)
tentativas = 0

chute = int(input("Digite o seu numero: "))

while chute != numero_secreto:
    if chute != numero_secreto and chute > numero_secreto:
        print("Você errou, tente novamente")
        print("Dica: o numero que ditado é maior que o numero secreto")
        chute = int(input("Digite o seu numero novamente: "))
        tentativas += 1
    elif chute != numero_secreto and chute < numero_secreto:
        print("Você errou, tente novamente")
        print("Dica: o numero que ditado é menor que o numero secreto")
        chute = int(input("Digite o seu numero novamente: "))
        tentativas += 1

print()
print("***********************")
print("Você venceu!")
print("Você digitou: ", chute)
print("O numero secreto era: ", numero_secreto)
print("Numero de tentativas: ", tentativas)
print("Fim do jogo!")
print("***********************")
