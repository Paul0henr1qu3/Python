#/usr/bin/env python3.4
# _*_ coding: UTF_8 _*_
'''
Classe representando uma Conta Corrente
'''
import conta

class ContaCorrente(conta):

    def __saca(self, valor):

        valor = valor + (valor * 0.10)

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
