#!/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
"""
Jogo de Dados
Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
"""

from random import randint

print("Jogo de Dados")
print("Teste sua sorte")

while(True):
    numero = int(input("Escolha um número: "))
    dados = randint(1,6)
    if numero == dado:
        print("Parabéns, saiu o seu número no dado.")
    else:
        print("Não foi dessa vez.")
        print("O número sorteado foi: ")
        print(dado)
    print("Deseja tentar a sorte novamente?")
    continuar = input("Digite S para continuar ou N para sair: ")

    if continuar == 'N' or continuar == 'n':
        break
