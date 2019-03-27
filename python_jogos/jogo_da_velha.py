#!/usr/bin/env python3.4
# _*_ coding: UTF-8 _*_
"""
Um jogo da velha simples
Desenvolvido por: paul0henr1qu3 -> https://github.com/Paul0henr1qu3
Versão: 0.0.1
"""

from curses import initscr, wrapper
from random import randint

def boas_vindas(stdscr):
    #A medida  que descemms na tela o valor de y cresce, no caso o primeiro valor.
    stdscr.addstr(1, 1, "Bem vindo ao Jogo da Velha.")
    stdscr.addstr(2, 1, "Pressine Q para sair ou H para obter ajuda.")
    stdscr.addstr(16, 1, "Desenvolvido por: paul0henr1qu3.")
    stdscr.addstr(17, 1, "Licença Nova BSD")

def ajuda(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 1, "Pressione Q para sair ou H para exibir essa ajuda.")
    stdscr.addstr(2, 1, "Para mudar a posição, use as teclas: A, D, S, W")
    stdscr.addstr(3, 1, "Para definir uma posição do jogo, digite: L")
    stdscr.addstr(4, 1, "Para reiniciar uma partida, digite: Y")
    stdscr.addstr(5, 1, "Pressione espaço para sair dessa tela.")
    stdscr.refresh()

def reiniciar_tela(stdscr, limpar=True):
    if limpar is True:
        #Comando para limpar a tela
        stdscr.clear()
    #Comando para criar um retângulo ou borda em nossa tela.
    stdscr.border()
    boas_vindas(stdscr)
    '''
    Comando refresh utilizado para indicar que queremos que todas as operações
    que fizemos no terminal possam ser exibidas na tela do usuário.
    '''
    stdscr.refresh()

#stdscr -> Terminal
#posicoes -> Lista de Posições
#x_center ->  Recebe o centro do terminal
def tabuleiro(stdscr, posicoes, x_center):
    stdscr.clear()
    reiniciar_tela(stdscr, limpar=False)

    #Desenhando linhas horizontais nas posições y = 10 e y = 12
    stdscr.addstr(10, x_center - 3, "-----")
    stdscr.addstr(12, x_center - 3, "-----")
    #Iniciando o tabuleiro na posição 9
    i=9

    for linha in posicoes:
        '''tela consiste em uma string contendo as informações de cada elemento
        da sublista que faz parte da lista posiçoes
        '''
        tela = "%s|%s|%s " % tuple(linha)
        stdscr.addstr(i, x_center - 3, tela)
        i += 2


'''Essa função está verificando se o jogador está se movendo dentro do
espaço do tabuleiro, definido por uma matriz 3x3.
'''
def limites(pos_x, pos_y):
    if pos_x > 2:
        pos_x = 0

    if pos_x < 0:
        pos_x = 2

    if pos_y > 2:
        pos_y = 0

    if pos_y < 0:
        pos_y = 2

    return pos_x, pos_y

#Receberá a posição corrente e a tela digita pelo usuário
def espaco_do_tabuleiro(pos_x, pos_y, entrada):
    if entrada == 'a':
        pos_x, pos_y = limites(pos_x -1, pos_y)
    elif entrada == 'd':
        pos_x, pos_y = limites(pos_x + 1, pos_y)
    elif entrada == 's':
        pos_x, pos_y = limites(pos_x, pos_y + 1)
    elif entrada == 'w':
        pos_x, pos_y = limites(pos_x, pos_y -1)
    else:
        pass

    return pos_x, pos_y

def cursor(stdscr, pos_x, pos_y, x_center):

    cursor_y = 9
    cursor_x = x_center - 3
    if pos_y == 1:
        cursor_y += 2

    if pos_y == 2:
        cursor_y += 4

    if pos_x == 1:
        cursor_x += 2

    if pos_x == 2:
        cursor_x += 4

    # A atualização do cursor na tela foi feita usando o comando .move
    stdscr.move(cursor_y, cursor_x)

'''
O que essa função fará é verificar se na lista posicoes tem um espaço em
branco e, se for verdade vai substituir  esse espaço por um X.
'''
def jogador(pos_x, pos_y, posicoes):
    if posicoes[pos_y][pos_x] == " ":
        posicoes[pos_y][pos_x] = "x"
        return True, posicoes
    return False, posicoes

#A função tobo, vai receber uma lista contento as posições da jogada corrente
def robo(posicoes):

    vazias = []
    #Pegando as posições que ainda não foram preenchidas e guardando na lista
    for i in range(0,3):
        for j in range(0,3):
            if posicoes[j][i] == " ":
                vazias.append([j, i])

    n_escolhas = len(vazias)

    if n_escolhas != 0:
        #Selecionando uma posiação aleatória vazia e preenchendo com o valor "O"
        j, i = vazias[randint(0, n_escolhas - 1)]
        posicoes[j][i] = "O"

    return posicoes

def total_alinhado(linha):
    num_x = linha.count("X")
    num_o = linha.count("O")

    if num_x == 3:
        return "X"

    if num_o == 3:
        return "O"

    return None

def ganhador(posicoes):
    diagonal1 = [posicoes[0][0], posicoes[1][1], posicoes[2][2]]
    diagonal2 = [posicoes[0][2], posicoes[1][1], posicoes[2][0]]

    transposta = [[], [], []]
    '''
    Um laço alinhado no qual, para cada linha i da matriz transposta, indicamos
    que queremos adicionar um elemento [j][i] da matriz posicoes
    '''
    for i in range(3):
        for j in range(3):
            transposta[i].append(posicoes[j][i])

    gan = total_alinhado(diagonal1)
    if gan is not None:
        return gan

    gan = total_alinhado(diagonal2)
    if gan is not None:
        return gan

    velha = 9
    for i in range(3):

        gan = total_alinhado(posicoes[i])
        if gan is not None:
            return gan

        gan = total_alinhado(transposta[i])
        if gan is not None:
            return gan

        velha -= posicoes[i].count("X")
        velha -= posicoes[i].count("O")

    if velha == 0:
        return "Velha"

    return None

def fim_de_jogo(stdscr, vencedor):
    stdscr.addstr(6, 1, "O %s venceu..." % vencedor)
    stdscr.addstr(7, 1, "Pressione Y para jogar novamente ou Q para sair.")

    stdscr.refresh()

#A variavel stdscr representa a nossa tela padrão
def main(stdscr):

    reiniciar_tela(stdscr)
    #getmaxxy é utilizada para obter a altura e largura do Terminal
    #[1] é utilizado para pegar apenas informação necessária
    width = stdscr.getmaxyx()[1]
    '''Calculando o centro como sendo a divisão inteira, por dois, da largura
    menos um, feito usando o operador de divisão inteira //
    '''
    x_center = (width - 1) // 2

    posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    pos_x, pos_y = 0, 0

    fim_de_partida = None

    '''
    O coração de todo jogo é o laço infinito que só será interrompido quando
    o jogador quiser encerrar o jogo,
    '''
    while True:
        #O Metódo getkey() pega a informação digitada pelo usuário
        entrada = stdscr.getkey()
        if entrada == 'q':
            break

        if fim_de_partida is None:

            if entrada in ['a', 's', 'w', 'd']:
                pos_x, pos_y = espaco_do_tabuleiro(pos_x, pos_y, entrada)

            if entrada  == "\n":
                jogou, posicoes = jogador(pos_x, pos_y, posicoes)
                fim_de_partida = ganhador(posicoes)
                if jogou is True and fim_de_partida is None:
                    posicoes = robo(posicoes)

        if entrada == 'y':
            fim_de_partida = None
            posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            pos_x, pos_y = 0, 0

        if entrada == 'h':
            ajuda(stdscr)
        else:
            tabuleiro(stdscr, posicoes, x_center)
            '''para que nossa função cursor funcione, ela sempre deve ser a última
            a ser chamada, logo após o desenho de todo o resto na tela.
            '''
            if fim_de_partida is not None:
                fim_de_jogo(stdscr, fim_de_partida)
            cursor(stdscr, pos_x, pos_y, x_center)

#Esse if só sera executado se o nosso arquivo for o programa principal
#A função initscr será usada apenas para inicializarmos o nosso terminal.
'''Já a função wrapper será usada para encapsular a função  principal do jogo,
para que possamos ter acesso ás facilidades desse módulo'''
if __name__ == "__main__":
    #Faz a inicialização da nossa tela padrão(Inicia o terminal do jogo)
    initscr()
    '''
    Essa chamada está indicando para o modulo curse que quem vai fazer
    a manipulação do terminal do jogo é a função __main__
    '''
    wrapper(main)
