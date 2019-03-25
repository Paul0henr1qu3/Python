#/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
'''
ExerciciosFuncoes: https://wiki.python.org.br/ExerciciosFuncoes

1.Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

Programa sob licença GNU V.3
Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
'''

def sequencial(n):

    i = 1
    while i <= n:
        numero_convertido = str(i) + " "
        print numero_convertido * i
        print
        i += 1

numero = int(input("Digite um numero: "))
sequencial(numero)
