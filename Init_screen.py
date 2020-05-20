import pygame
import random
import os
from Configuração import IMG_DIR, FPS, JOGANDO, FINAL
from Assets import *

def init_screen(screen):
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()
    assets = load_assets()

    # Carrega o fundo da tela inicial
    fundo = assets[INIT_FUNDO]
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
                estado = FINAL
                running = False

            if event.type == pygame.KEYUP:
                estado = JOGANDO
                running = False

        # A cada loop, redesenha o fundo
        screen.blit(fundo, fundo_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado