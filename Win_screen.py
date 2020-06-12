""" O arquivo Win_screen.py será utilizada para carregar a tela quando o jogador ganha o jogo """
# Importa as bibliotecas do jogo
import pygame
import random
import os

# Importa os arquivos do jogo
from Configuracao import *
from Assets import *

def win_screen(screen, assets):
    """ Função que carrega a imagem e o som de vitória """
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()

    # Inicia o som
    assets[SOM_VITORIA].play()
    
    # Define uma condição para as telas de vitória apareçam
    running = True
    i = 0

    # Enquanto a tela de vitória está rodando
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(10)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                # Muda o estado da tela e fecha o jogo
                estado = QUIT
                # Interrompe a tela de vitória e fecha o jogo
                running = False

        # Desenha a tela de vitória
        screen.blit(assets[GANHANDO_ANIM][i], (0, 0))

        # Adiciona as imagens da animação de vitória
        if i < 67:
            i += 1
 
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    # Retorna o estado do jogo
    return estado