#!/usr/bin/env python3.4
# _*_coding: UTF-8 _*_
'''
Simples jogo de forca.
'''

def forca(palavra):
    print("|--------------------")
    print("|                   |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|" + "_ " * len(palavra))

def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')


    palavra_secreta = "relogios".capitalize()
    forca(palavra_secreta)

    enforcou = False
    acertou = False

    index = 0
    while not acertou and not enforcou:
        chute = input("Qual a letra?").strip()

        for letra in palavra_secreta:
            if letra == chute.lower():
                print("Encontrei a letra {} na posição {}".format(chute, index))

            index += 1


        break

if(__name__ == "__main__"):
    jogar()
