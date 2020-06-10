""" O arquivo Tela_Principal.py que será utilizado pelo jogador para o jogo completo (tela inicial, jogo, tela de game over e tela de vitória) """

# Importa as bibliotecas necessárias
import pygame
import random
import os

# Importa os arquivos do jogo
from Configuracao import *
from Init_screen import init_screen
from Game_Screen import game_screen
from Lose_screen import end_screen
from Win_screen import win_screen
from Assets import load_assets

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Super Peach Sis')

# Carrega os assets
assets = load_assets()

estado = INICIO
while estado != QUIT:
    if estado == INICIO:
        estado = init_screen(window, assets)
    elif estado == JOGO:
        estado = game_screen(window, assets)
    elif estado == LOSE:
        estado = end_screen(window, assets)
    elif estado == WIN:
        estado = win_screen(window, assets)
    else:
        estado = QUIT
# ===== Finalização =====
pygame.quit()