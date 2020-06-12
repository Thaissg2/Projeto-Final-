""" O arquivo Instrucoes_Screen.py carrega a tela de instruções do jogo"""

# Importa as bibliotecas do jogo
import pygame
import random
import os

# Importa os arquivos do jogo
from Configuracao import *
from Assets import *

def instrucoes_screen(screen, assets):
    """ Função que carrega a imagem de instruções do jogo """
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()

    # Carrega a tela de instruções e a configura de acordo o tamanho da janela
    fundo = assets[INSTRUCOES_IMG]
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
    fundo_rect = fundo.get_rect()

    # Define uma condição para a tela inicial aparecer
    running = True

    # Enquanto a tela de instruções está rodando
    while running:
        # Ajusta a velocidade do jogo
        clock.tick(FPS)
        # Processa os eventos
        for event in pygame.event.get():
            # Verifica se jogo foi fechado
            if event.type == pygame.QUIT:
                # Muda o estado e fecha o jogo
                estado = QUIT
                # Interrompe a tela de início e fecha o jogo
                running = False
            # Verifica se o jogador clicou em alguma tecLa
            if event.type == pygame.KEYUP:
                # Muda o estado para o jogo
                estado = JOGO
                # Interrompe a tela de início e fecha o jogo
                running = False
        # A cada loop, redesenha o fundo
        screen.blit(fundo, fundo_rect)

        # Depois de desenhar tudo, inverte o display
        pygame.display.flip()

    # Retorna o estado do jogo
    return estado