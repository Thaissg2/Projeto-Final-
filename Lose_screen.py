import pygame
import random
import os
from Configuracao import *
from Assets import *

def end_screen(screen, assets):
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    fundo = assets[GAMEOVER_FUNDO]
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
    fundo_rect = fundo.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Inicia o som
        assets[TRILHA_SONORA].stop()
        assets[SOM_ESPINHO_GIGANTE].stop
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

    return estado