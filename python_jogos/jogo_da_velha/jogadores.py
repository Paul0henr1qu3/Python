#/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
"""
Módulo responsável por genrenciar os Jogadores
"""

from random import randint

class Jogadores(object):

    def __init__(self, controle, posicoes):
        self.controle = controle
        self.posicoes = posicoes
        self.fim_de_partida = False
        self._vencedor = None

    def jogador(self):
        if self.posicoes[self.controle.pos_y][self.controle.pos_x] == " ":
            self.posicoes[self.controle.pos_y][self.controle.pos_x] = "x"
            return True
        return False

    #A função tobo, vai receber uma lista contento as posições da jogada corrente
    def robo(self):

        vazias = []
        #Pegando as posições que ainda não foram preenchidas e guardando na lista
        for i in range(0,3):
            for j in range(0,3):
                if self.posicoes[j][i] == " ":
                    vazias.append([j, i])

        n_escolhas = len(vazias)

        if n_escolhas != 0:
            #Selecionando uma posiação aleatória vazia e preenchendo com o valor "O"
            j, i = vazias[randint(0, n_escolhas - 1)]
            self.posicoes[j][i] = "O"


    def _total_alinhado(self, linha):
        num_x = linha.count("X")
        num_o = linha.count("O")

        if num_x == 3:
            return "X"

        if num_o == 3:
            return "O"

        return None

    def ganhador(self):
        diagonal1 = [self.posicoes[0][0], self.posicoes[1][1], self.posicoes[2][2]]
        diagonal2 = [self.posicoes[0][2], self.posicoes[1][1], self.posicoes[2][0]]

        transposta = [[], [], []]
        '''
        Um laço alinhado no qual, para cada linha i da matriz transposta, indicamos
        que queremos adicionar um elemento [j][i] da matriz posicoes
        '''
        for i in range(3):
            for j in range(3):
                transposta[i].append(self.posicoes[j][i])

        gan = self._total_alinhado(diagonal1)
        if gan is not None:
            self._vencedor = gan
            return True

        gan = self._total_alinhado(diagonal2)
        if gan is not None:
            self._vencedor = gan
            return True

        velha = 9
        for i in range(3):

            gan = self._total_alinhado(self.posicoes[i])
            if gan is not None:
                self._vencedor = gan
                return True

            gan = self._total_alinhado(transposta[i])
            if gan is not None:
                self._vencedor = gan
                return True

            velha -= self.posicoes[i].count("X")
            velha -= self.posicoes[i].count("O")

        if velha == 0:
            self._vencedor = "Velha"
            return True

        return False

    def jogar(self):
        jogou = self.jogador()
        self.fim_de_partida = self.ganhador()

        if jogou is True and self.fim_de_partida is False:
            self.robo()
            self.fim_de_partida = self.ganhador()


    def _set_vencedor(self, vencedor):
        self._vencedor = vencedor

    def _get_vencedor(self):
        return self._vencedor

    vencedor = property(_get_vencedor, _set_vencedor)
