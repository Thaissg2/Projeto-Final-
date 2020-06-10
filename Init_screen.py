# Importa as bibliotecas do jogo
import pygame
import random
import os

# Importa os arquivos do jogo
from Configuracao import *
from Assets import *

def init_screen(screen, assets):
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()

    # Carrega o background e o configura de acordo o tamanho da janela
    fundo = assets[INIT_FUNDO]
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
    fundo_rect = fundo.get_rect()

    # Define uma condição para a tela inicial aparecer
    running = True

    while running:
        # Ajusta a velocidade do jogo
        clock.tick(FPS)
        # Processa os eventos
        for event in pygame.event.get():
            # Verifica se jogo foi fechado
            if event.type == pygame.QUIT:
                estado = QUIT
                # Interrompe a tela de início e fecha o jogo
                running = False
            # Verifica se o jogador clicou em alguma teca
            if event.type == pygame.KEYUP:
                estado = JOGO
                # Interrompe a tela de início e fecha o jogo
                running = False
        # A cada loop, redesenha o fundo
        screen.blit(fundo, fundo_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado