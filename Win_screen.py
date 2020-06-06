import pygame
import random
import os
from Configuracao import *
from Assets import *

def win_screen(screen):
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()
    assets = load_assets()

    # Carrega o fundo da tela inicial
    fundo = assets[GANHANDO_ANIM]

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Inicia o som
        assets[TRILHA_SONORA].stop()
        assets[SOM_ESPINHO_GIGANTE].stop
        assets[SOM_VITORIA].play()
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                estado = QUIT
                running = False

        # Desenha a tela de game over
        screen.blit(assets[GANHANDO_ANIM], fundo)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado