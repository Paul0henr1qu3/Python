#!/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
"""
Módulo principal do Jogo
"""


from curses import initscr, wrapper
from tela import Tela
from controle import Controle
from jogadores import Jogadores
from dado import Dado

def main(stdscr):

    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    controle = Controle(stdscr=stdscr)
    tela = Tela(stdscr=stdscr, posicoes=posicoes)
    jogadores = Jogadores(controle=controle, posicoes=posicoes)
    tela.reiniciar_tela()
    dado = Dado()

    jogador_x = 0
    jogador_o = 0

    while True:

        controle.espaco_do_tabuleiro()

        if jogadores.fim_de_partida is False:
            if controle.entrada == "\n":
                jogadores.jogar()

            if jogadores.fim_de_partida is True:
                ganhador = jogadores.vencedor
                if ganhador == "X":
                    jogador_x += 1
                if ganhador == "O":
                    jogador_o += 1

        if controle.entrada == "y":
            for i in range(3):
                for j in range(3):
                    posicoes[i][j] = " "

            controle.pos_y = 0
            controle.pos_x = 0
            jogadores.vencedor = None
            jogadores.fim_de_partida = False
            tela.reiniciar_tela()

        if controle.entrada == 'h':
            tela.ajuda()
        else:
            tela.tabuleiro(controle)
            tela.placar(jogador_x, jogador_o)
            if jogadores.fim_de_partida is True:
                tela.fim_de_jogo(jogadores.vencedor)
            controle.cursor()

if __name__== "__main__":
    initscr()
    wrapper(main)
