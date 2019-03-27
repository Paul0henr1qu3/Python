#!/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_

import forca
import adivinhacao

print("***********************************")
print("********Escolha o seu Jogo!********")
print("***********************************")

print("(1) Forca (2) Adivinhacao")

jogo = int(input("Qual o Jogo?"))

if jogo == 1:
    print("Jogando Forca")
    forca.jogar()
else jogo == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()
