#/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
'''
ExerciciosListas: https://wiki.python.org.br/ExerciciosListas
17.
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m


Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
'''

def imprimiSaltos(lista):
    if len(lista) >= 5:
        return "{0} - {1} - {2} - {3} - {4}".format(lista[0], lista[1], lista[2], lista[3], lista[4])

atleta = input("Digite o nome do Atleta: ")

saltos = []

for i in range(1,6):
    salto = int(input("Digite o {0}º: ".format(i)))
    saltos.append(salto)

print("\nResultado final:")
print("Atleta: {0}".format(atleta))
print("Saltos: ", imprimiSaltos(saltos))
print("Media: {0}".format(sum(saltos)/5))
