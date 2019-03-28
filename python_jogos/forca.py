#!/usr/bin/env python3.4
# _*_coding: UTF-8 _*_
'''
Simples jogo de forca.
'''
import random

'''
import urllib
f = urllib.urlopen('http://www.google.com.br/search?q=﻿'+ palavra_secreta)

    print(f)

    f.close()
    
implementar uma função para buscar uma dica da palavra secreta no google. 


'''

def forca(lista_acertos):
    print("|--------------------")
    print("|                   |")
    print("|")
    print("|")
    print("|")
    print("|")
    print(lista_acertos)


def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    with open("palavras.txt", "r") as arquivo:
        palavras = [palavra.strip() for palavra in arquivo]


    palavra = random.choice(palavras)
    palavra_secreta = palavra.upper()

    letras_acertadas = ["_ " for letra in palavra_secreta ]

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
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()
