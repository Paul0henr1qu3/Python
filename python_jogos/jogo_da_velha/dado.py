#!/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
'''
Classe que joga os dados para os jogadores decidirem quem irá iniciar a partida.
Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
'''

from random import randint

class Dado(object):

    def joga_o_dado(self):

        numero_robo = radint(1,6)
        numero_dado = randint(1,6)

        while True:
            if numero_user == numero_dado:
                return True
            if numero_robo == numero_dado:
                return False
