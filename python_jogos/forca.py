#!/usr/bin/env python3.4
# _*_coding: UTF-8 _*_
'''
Simples jogo de forca.
'''
import random

def apresentacao():

    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

def palavra(arquivo="palavras.txt"):

    with open(arquivo, "r") as arquivo:
        palavras = [palavra.strip() for palavra in arquivo]


    palavra = random.choice(palavras)

    return palavra.upper()

def inicializa(palavra):

    return ["_ " for letra in palavra]

def chutes():
    chute = input("\nQual a letra?").strip().upper()
    return chute

def acertos(chute, palavra, letras):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras[index] = letra
            letras_faltando = str(letras.count("_ "))
            print("Ainda faltam acertar {} letras".format(letras_faltando))
        index += 1

def vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    apresentacao()
    palavra_secreta = palavra()
    letras_acertadas = inicializa(palavra_secreta)

    erros = 0

    print(letras_acertadas)

    while True:
        chute = chutes()

        if chute in palavra_secreta:
            acertos(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_acertadas)

        if erros == len(palavra_secreta):
            break
        if "_ " not in letras_acertadas:
            break



    if "_ " not in letras_acertadas:
        vencedor()
    else:
        perdedor(palavra_secreta)

if(__name__ == "__main__"):
    jogar()
