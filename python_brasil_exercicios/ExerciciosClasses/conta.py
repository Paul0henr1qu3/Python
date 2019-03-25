#/usr/bin/env python3.4
# _*_ coding: UTF_8 _*_
'''
Classe representando uma Conta
'''

class Conta(object):

    def __init__(self, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):

        valor = valor + (valor * 0.10)

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def saldo(self):
        print("Saldo: ", self.saldo)
