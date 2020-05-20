import pygame
import random
import os
from Configuração import LARGURA, ALTURA, INICIO, JOGO, QUIT
from Init_screen import init_screen
from Game_Screen import game_screen

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
    #elif state == END:
    #    estado = end_screen(window)
    else:
        estado = QUIT
# ===== Finalização =====
pygame.quit()