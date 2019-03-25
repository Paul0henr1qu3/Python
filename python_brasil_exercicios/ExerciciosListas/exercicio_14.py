#!/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
"""
ExerciciosListas: https://wiki.python.org.br/ExerciciosListas

14.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

Programa sob licença GNU V.3
Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
"""

interrogatorio = ["Telefonou para a vítima?", "Esteve no local do crime?",
"Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" ]
respostas = []
count_classifica = 0

print("------------------------")
print("Interrogatório do Crime.")
print("------------------------")

for pergunta in interrogatorio:
    resposta = input(pergunta + ": ")
    respostas.append(resposta)

for resposta in respostas:
    if resposta.lower() == "sim":
        count_classifica += 1

if count_classifica == 2:
    print("\nRelatório da análise: Suspeita")
elif count_classifica >=  3 or count_classifica <= 4:
    print("\nRelatório da análise: Cúmplice")
elif count_classifica == 5:
    print("\nRelatório da análise: Assassino")
else:
    print("\nRelatório da análise: Inocente")
