import pygame
import random
import os
from Configuracao import *
from Assets import *

def win_screen(screen, assets):
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()

    # Inicia o som
    assets[SOM_VITORIA].play()
    
    # Carrega o fundo inicial
    running = True
    i = 0
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(10)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                estado = QUIT
                running = False

        # Desenha a tela de vitória
        screen.blit(assets[GANHANDO_ANIM][i], (0, 0))

        # Adiciona as imagens da animação de vitória
        if i < 67:
            i += 1   
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado