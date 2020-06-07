import pygame
import random
import os
from Configuracao import *
from Init_screen import init_screen
from Game_Screen import game_screen
from Lose_screen import end_screen
from Win_screen import win_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Super Peach Sis')

estado = INICIO
while estado != QUIT:
    if estado == INICIO:
        estado = init_screen(window)
    elif estado == JOGO:
        estado = game_screen(window)
    elif estado == LOSE:
        estado = end_screen(window)
    elif estado == WIN:
        estado = win_screen(window)
    else:
        estado = QUIT
# ===== Finalização =====
pygame.quit()