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
        assets[SOM_ESPINHO_GIGANTE].stop()
        assets[SOM_VITORIA].play()
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                estado = QUIT
                running = False

        # Desenha a tela de game over
        ganhando_anim = []
        for i in range(1,69):
            arquivo_anim = os.path.join(IMG_DIR, 'Slide{}.PNG'.format(i))
            fundo = pygame.image.load(arquivo_anim)
            fundo= pygame.transform.scale(fundo, (LARGURA, ALTURA))
            ganhando_anim.append(fundo)
            assets[GANHANDO_ANIM] = ganhando_anim
            screen.blit(assets[GANHANDO_ANIM][i], fundo)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado