#/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
"""

Modulo contendo a classe construtora de carros
"""

class Carro(object):

    def __init__(self, cor, potencia, modelo, marca):
        self.cor = cor
        self.potencia = potencia
        self.modelo = modelo
        self.marca = marca
        self._velocidade = 0

    #Utilizando __ estamos dizendo que o metodo é super protegido
    def __atualiza_velocidade(self, valor):
        self._velocidade = valor

    def acelera(self):
        self.__atualiza_velocidade(valor=10)
        print("Vruuum")

    def freiar(self):
        self.__atualiza_velocidade(valor=0)
        print("Parando")
