""" O arquivo Lose_screen.py será utilizada para carregar a tela quando o jogador perde o jogo """

# Importa as bibliotecas do jogo
import pygame
import random
import os

# Importa os arquivos do jogo
from Configuracao import *
from Assets import *

def end_screen(screen, assets):
    """ Função que carrega a imagem e o som de game over """
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    fundo = assets[GAMEOVER_FUNDO]
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
    fundo_rect = fundo.get_rect()

    # Define uma condição para a tela de game over aparecer
    running = True
    
    # Enquanto a tela de game over está rodando
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Inicia o som
        assets[SOM_TELA_GAMEOVER].play()

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                estado = QUIT
                running = False

        # Desenha a tela de game over
        screen.blit(assets[GAMEOVER_FUNDO], fundo_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    # Retorna o estado do jogo
    return estado