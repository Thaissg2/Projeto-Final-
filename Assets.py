import pygame
import os
from Configuração import *

FUNDO = 'fundo'
INIT_FUNDO = 'init_fundo'
ESPINHO_IMG = 'espinho_img'
PLATAFORMA_IMG = 'plataforma_img'
PEACH_IMG = 'peach_img'
BLOCO_IMG = 'bloco_img'
COGUMELO_IMG ='cogumelo_img'
ESPINHO_GIGANTE_IMG = 'espinho_gigante_img'

TRILHA_SONORA = 'trilha_sonora'
SOM_MORTE = 'som_morte'
SOM_COGUMELO = 'som_cogumelo'
SOM_DANO = 'som_dano'

PISCANDO_ANIM = 'piscando_anim'

CORACAO = 'coracao'

def load_assets():
    # Carrega as imagens do jogo e configura os tamanhos
    assets = {}

    assets[FUNDO] = pygame.image.load(os.path.join(IMG_DIR, 'fundo2.jpg')).convert()
    assets[FUNDO] = pygame.transform.scale(assets['fundo'], (LARGURA, ALTURA))

    assets[INIT_FUNDO] = pygame.image.load(os.path.join(IMG_DIR, 'tela_inicio.jpg')).convert()
    assets[INIT_FUNDO] = pygame.transform.scale(assets['init_fundo'], (LARGURA, ALTURA))

    assets[ESPINHO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'espinho2.png')).convert_alpha()
    assets[ESPINHO_IMG] = pygame.transform.scale(assets['espinho_img'], (ESPINHO_LARGURA, ESPINHO_ALTURA))
    
    assets[PLATAFORMA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'plataforma.png')).convert_alpha()
    assets[PLATAFORMA_IMG] = pygame.transform.scale(assets['plataforma_img'], (PLATAFORMA_LARGURA, PLATAFORMA_ALTURA))

    assets[PEACH_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Peach2.png')).convert_alpha()
    assets[PEACH_IMG] = pygame.transform.scale(assets['peach_img'], (PEACH_LARGURA, PEACH_ALTURA))
    
    assets[BLOCO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bloco.jpg')).convert_alpha()
    assets[BLOCO_IMG] = pygame.transform.scale(assets['bloco_img'], (BLOCO_TAMANHO, BLOCO_TAMANHO))
    
    assets[COGUMELO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'cogumelo.png')).convert_alpha()
    assets[COGUMELO_IMG] = pygame.transform.scale(assets['cogumelo_img'], (COGUMELO_LARGURA, COGUMELO_ALTURA))

    assets[ESPINHO_GIGANTE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'espinho2.png')).convert_alpha()
    assets[ESPINHO_GIGANTE_IMG] = pygame.transform.scale(assets['espinho_gigante_img'], (GIGANTE_LARGURA, GIGANTE_ALTURA))

    # Carrega as animações do jogo
    # Define animmação do dano
    piscando_anim = []
    for i in range(0,8):
        arquivo_anim = os.path.join(IMG_DIR, 'piscando{}.png'.format(i))
        imagem = pygame.image.load(arquivo_anim).convert_alpha()
        imagem = pygame.transform.scale(imagem, (75, 125))
        piscando_anim.append(imagem)
    assets[PISCANDO_ANIM] = piscando_anim

    # Carrega a imagem da vida do jogador
    assets[CORACAO] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    assets[TRILHA_SONORA] = pygame.mixer.Sound(os.path.join(SND_DIR, 'trilha_sonora1.wav'))
    assets[SOM_MORTE] = pygame.mixer.Sound(os.path.join(SND_DIR, 'morte.wav'))
    assets[SOM_COGUMELO] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som_cogumelo.wav'))
    assets[SOM_DANO] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som_dano.wav'))
    
    return assets