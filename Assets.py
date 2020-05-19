import pygame
import os
from Configuração import ESPINHO_LARGURA, ESPINHO_ALTURA, PLATAFORMA_LARGURA, PLATAFORMA_ALTURA, PEACH_LARGURA, PEACH_ALTURA, BLOCO_TAMANHO, COGUMELO_ALTURA, COGUMELO_LARGURA, GIGANTE_ALTURA, GIGANTE_LARGURA, IMG_DIR, SND_DIR, FNT_DIR

FUNDO = 'fundo'
ESPINHO_IMG = 'espinho_img'
ESPINHO_IMG = 'espinho_img'
PLATAFORMA_IMG = 'plataforma_img'
PLATAFORMA_IMG = 'plataforma_img'
PEACH_IMG = 'peach_img'
PEACH_IMG = 'peach_img'
BLOCO_IMG = 'bloco_img'
BLOCO_IMG = 'bloco_img'
COGUMELO_IMG ='cogumelo_img'
COGUMELO_IMG ='cogumelo_img'
ESPINHO_GIGANTE_IMG = 'espinho_gigante_img'
ESPINHO_GIGANTE_IMG = 'espinho_gigante_img'
TRILHA_SONORA = 'trilha_sonora'
SOM_MORTE = 'som_morte'
SOM_COGUMELO = 'som_cogumelo'
SOM_DANO = 'som_dano'

def load_assets():
    # Carrega as imagens do jogo
    assets = {}
    assets[FUNDO] = pygame.image.load(os.path.join(IMG_DIR, 'fundo2.png')).convert_alpha()
    assets[ESPINHO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'espinho2.png')).convert_alpha()
    assets[PLATAFORMA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'plataforma.png')).convert_alpha()
    assets[PEACH_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Peach2.png')).convert_alpha()
    assets[BLOCO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bloco.jpg')).convert_alpha()
    assets[COGUMELO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'cogumelo.png')).convert_alpha()
    assets[ESPINHO_GIGANTE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'espinho2.png')).convert_alpha()

    # Carrega as animações do jogo
    piscando_anim = []
    for i in range(0,8):
        # Definindo animmação do dano
        arquivo_anim = os.path.join(IMG_DIR, 'piscando{}.png'.format(i)
        img = pygame.image.load(arquivo_anim).convert_alpha()
        img = pygame.transform.scale(img, (75, 125))
        piscando_anim.append(img)
    assets[PISCANDO_ANIM] = piscando_anim

    # Carrega os sons do jogo
    assets[TRILHA_SONORA] = pygame.mixer.Sound(os.path.join(SND_DIR, 'trilha_sonora1.wav'))
    assets[SOM_MORTE] = pygame.mixer.Sound(os.path.join(SND_DIR, 'morte.wav'))
    assets[SOM_COGUMELO] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som_cogumelo.wav'))
    assets[SOM_DANO] = pygame.mixer.Sound(os.ath.join(SND_DIR, 'som_dano.wav')
    return assets