#/usr/bin/env python3.4
# _*_ coding: UTF_8 _*_
'''
Classe Bola
''' 

class Bola(object):

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print("Cor: ", self.cor)
