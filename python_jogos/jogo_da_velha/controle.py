#/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
'''
Módulo responsável por controlar as ações do jogo
'''

'''
Esse módulo é  usado para ter acesso a algumas variáveis usadas ou mantidas
pelo interpretador, além de fornecer acesso a funções com maior poder de
interação com o interpretador.
'''
import sys

class Controle(object):

    def __init__(self, stdscr):
        self.stdscr = stdscr
        width = stdscr.getmaxyx()[1]
        self.x_center = (width -1) // 2
        self.pos_x = 0
        self.pos_y = 0
        self.entrada = None

    def _limites(self):

        if self.pos_x > 2:
            self.pos_x = 0
        if self.pos_x < 0:
            self.pos_x = 2

        if self.pos_y > 2:
            self.pos_y = 0
        if self.pos_y < 0:
            self.pos_y = 2

    def espaco_do_tabuleiro(self,dado):

        self.entrada = self.stdscr.getkey()

        if self.entrada == 'q':
            sys.exit(0)

        if self.entrada in range(1,6):
            dado(self.entrada)

        if self.entrada == 'a':
            self.pos_x -= 1
        elif self.entrada == 'd':
            self.pos_x += 1
        elif self.entrada == 's':
            self.pos_y -= 1
        elif self.entrada == 'w':
            self.pos_y += 1
        else:
            pass

        self._limites()

    def cursor(self):

        cursor_y = 9
        cursor_x = self.x_center - 3
        if self.pos_y == 1:
            cursor_y += 2

        if self.pos_y == 2:
            cursor_y += 4

        if self.pos_x == 1:
            cursor_x += 2

        if self.pos_x == 2:
            cursor_x += 4

        # A atualização do cursor na tela foi feita usando o comando .move
        self.stdscr.move(cursor_y, cursor_x)
