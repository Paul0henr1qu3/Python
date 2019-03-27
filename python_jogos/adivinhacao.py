#/ussr/bin/env python3.4
# _*_ coding: UTF-8 _*_
'''
Simples Jogo de Adivinhacação
Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
'''

from random import randint
def jogar():
    print("***********************************")
    print("Bem vindo no jogo de Adivinhacação!")
    print("***********************************")

    numero_secreto = randint(1,100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificudade?")
    print("(1) - Fácil (2) - Médio (3) - Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")

        print("Voce digitou: " , chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if(acertou):
            print("Você acertou e fez {0}".format(pontos))
            break
        elif(maior):
            print("Você errou! O seu chute foi maior que o numero secreto")
            pontos_perdidos = chute - pontos_perdidos
            pontos = pontos - pontos_perdidos
        else:
            print("Você errou! O seu chute foi menor que o numero secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if __name__ == "__main__":
    jogar()
