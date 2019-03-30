#!/usr/bin/env python3.7
# _*_ coding: UTF-8 _*_
'''
ExerciciosListas: https://wiki.python.org.br/EstruturaDeDecisao

3.Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
'''

sexo = input('Digite o sexo F/M: ')

if sexo.upper() == 'F':
    print("{} - Feminino".format(sexo))
elif sexo.upper() == 'M':
    print("{} - Masculino".format(sexo))
else:
    print("Valor inválido!")
