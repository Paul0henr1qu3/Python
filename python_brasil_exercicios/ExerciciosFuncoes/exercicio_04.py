#/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
'''
ExerciciosListas: https://wiki.python.org.br/ExerciciosFuncoes
4.Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
'''

def pos_neg(n):
    if n > 0:
        return "P"
    else:
        return "N"

print(pos_neg(-1))
