import pygame
import random
import os
from Configuracao import *
from Assets import *

def end_screen(screen):
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()
    assets = load_assets()

    # Carrega o fundo da tela inicial
    fundo = assets[GAMEOVER_FUNDO]
    fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
    fundo_rect = fundo.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                estado = QUIT
                running = False

            if event.type == pygame.KEYUP:
                estado = LOSE
                running = False

        # A cada loop, redesenha o fundo
        screen.blit(assets[FUNDO], fundo_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return FINAL