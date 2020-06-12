""" O arquivo Tela_Principal.py que será utilizado pelo jogador para o jogo completo (tela inicial, instruções, jogo, tela de game over e tela de vitória) """

# Importa as bibliotecas necessárias
import pygame
import random
import os

# Importa os arquivos do jogo
from Configuracao import *
from Init_screen import init_screen
from Instrucoes_Screen import instrucoes_screen
from Game_Screen import game_screen
from Lose_screen import end_screen
from Win_screen import win_screen
from Assets import load_assets

# Inicializa o pygame
pygame.init()
pygame.mixer.init()

# Configura a largura e altura do tela
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Super Peach Sis')

# Carrega os assets
assets = load_assets()

# Estabelece o estado inicial do jogo
estado = INICIO

# Enquanto o jogador não fecha a tela
while estado != QUIT:
    # Verifica se o estado do jogo é INICIO
    if estado == INICIO:
        # Carrega a tela inicial do jogo
        estado = init_screen(window, assets)
    # Verifica se o estado do jogo é INSTRUCOES
    elif estado == INSTRUCOES:
        # Carrega a tela de instruções do jogo
        estado = instrucoes_screen(window, assets)
    # Verifica se o estado do jogo é JOGO
    elif estado == JOGO:
        # Carrega a tela em que o jogo acontece
        estado = game_screen(window, assets)
    # Verifica se o estado do jogo é LOSE
    elif estado == LOSE:
        # Carrega a tela de game over
        estado = end_screen(window, assets)
    # Verifica se o estado do jogo é WIN
    elif estado == WIN:
        # Carrega a tela de vitória
        estado = win_screen(window, assets)
    # Se não for nenhum dos estados anteriores:
    else:
        # Fecha a janela do jogo
        estado = QUIT

# ===== Finalização =====
pygame.quit()