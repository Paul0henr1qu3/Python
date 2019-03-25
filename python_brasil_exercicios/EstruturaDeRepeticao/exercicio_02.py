#/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
'''
EstruturaDeRepeticao: https://wiki.python.org.br/EstruturaDeRepeticao
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
'''
usuario = input("Usuário: ")
senha = input("Senha: ")

while usuario == senha:
    print("A senha não pode ser igual ao usuário, tente novamente!")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
