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

def palavra():

    with open("palavras.txt", "r") as arquivo:
        palavras = [palavra.strip() for palavra in arquivo]


    palavra = random.choice(palavras)

    return palavra.upper()

def inicializa(palavra):

    return ["_ " for letra in palavra]

def jogar():

    apresentacao()
    palavra_secreta = palavra()
    letras_acertadas = inicializa(palavra_secreta)

    erros = 0

    forca(letras_acertadas)

    while True:
        chute = input("\nQual a letra?").strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                    letras_faltando = str(letras_acertadas.count("_ "))
                    print("Ainda faltam acertar {} letras".format(letras_faltando))
                index += 1
        else:
            erros += 1
            print("Você ainda tem {} tentativas".format(len(palavra_secreta) - erros))

        if erros == len(palavra_secreta):
            break
        if "_ " not in letras_acertadas:
            break

        forca(letras_acertadas)

    if "_ " not in letras_acertadas:
        print(letras_acertadas)
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()
