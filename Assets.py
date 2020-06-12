""" O arquivo Assets.py configura as animações, sons e imagens presentes no jogo """

# Importa as bibliotecas necessárias
import pygame
import os

# Importa os arquivos
from Configuracao import *

# Define as variáveis da imagem
FUNDO = 'fundo'
INIT_FUNDO = 'init_fundo'
INSTRUCOES_IMG = 'instrucoes_img'
GAMEOVER_FUNDO = 'gameover_fundo'
ESPINHO_IMG = 'espinho_img'
PLATAFORMA_IMG = 'plataforma_img'
PEACH_IMG = 'peach_img'
BLOCO_IMG = 'bloco_img'
COGUMELO_IMG ='cogumelo_img'
ESPINHO_GIGANTE_IMG = 'espinho_gigante_img'
PLATAFORMA_MOVEL_IMG = 'plataforma_movel_img'
CHAVE_IMG = 'chave_img'

# Define as variáveis dos sons
TRILHA_SONORA = 'trilha_sonora'
SOM_MORTE = 'som_morte'
SOM_COGUMELO = 'som_cogumelo'
SOM_DANO = 'som_dano'
SOM_ESPINHO_GIGANTE = 'som_espinho_gigante'
SOM_TELA_GAMEOVER = 'som_tela_gameover'
SOM_VITORIA = 'som_vitoria'

# Define as variáveis das animações
PISCANDO_ANIM = 'piscando_anim'
DIMINUINDO_ANIM = 'dimunuindo_anim'
GANHANDO_ANIM = 'ganhando_anim'

# Define a variável da vida do jogador
CORACAO = 'coracao'

def load_assets():
    """ A função load_assets carrega as imagens que serão utilizadas em todo o jogo """
    assets = {}
        # Carrega imagem do background do jogo
    assets[FUNDO] = pygame.image.load(os.path.join(IMG_DIR, 'fundo2.jpg')).convert()
    assets[FUNDO] = pygame.transform.scale(assets['fundo'], (LARGURA, ALTURA))
        # Carrega a imagem da tela de início
    assets[INIT_FUNDO] = pygame.image.load(os.path.join(IMG_DIR, 'tela_inicio.jpeg')).convert()
    assets[INIT_FUNDO] = pygame.transform.scale(assets['init_fundo'], (LARGURA, ALTURA))
        # Carrega a imagem das instruções
    assets[INSTRUCOES_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'instrucoes.jpeg')).convert()
    assets[INSTRUCOES_IMG] = pygame.transform.scale(assets['instrucoes_img'], (LARGURA, ALTURA))
        # Carrega a imagem da tela de game over
    assets[GAMEOVER_FUNDO] = pygame.image.load(os.path.join(IMG_DIR, 'tela_gameover.jpeg')).convert()
    assets[GAMEOVER_FUNDO] = pygame.transform.scale(assets['gameover_fundo'], (LARGURA, ALTURA))
        # Carrega a imagem da plataforma 
    assets[PLATAFORMA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'plataforma.png')).convert_alpha()
    assets[PLATAFORMA_IMG] = pygame.transform.scale(assets['plataforma_img'], (PLATAFORMA_LARGURA, PLATAFORMA_ALTURA))
        # Carrega a imagem da personagem Peach
    assets[PEACH_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Peach2.png')).convert_alpha()
    assets[PEACH_IMG] = pygame.transform.scale(assets['peach_img'], (PEACH_LARGURA, PEACH_ALTURA))
        # Carrega a imagem dos blocos
    assets[BLOCO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bloco.jpg')).convert_alpha()
    assets[BLOCO_IMG] = pygame.transform.scale(assets['bloco_img'], (BLOCO_TAMANHO, BLOCO_TAMANHO))
        # Carrega a imagem dos cogumelos
    assets[COGUMELO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'cogumelo.png')).convert_alpha()
    assets[COGUMELO_IMG] = pygame.transform.scale(assets['cogumelo_img'], (COGUMELO_LARGURA, COGUMELO_ALTURA))
        # Carrega a imagem dos espinhos gigantes
    assets[ESPINHO_GIGANTE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'espinho2.png')).convert_alpha()
    assets[ESPINHO_GIGANTE_IMG] = pygame.transform.scale(assets['espinho_gigante_img'], (GIGANTE_LARGURA, GIGANTE_ALTURA))
        # Carrega a imagem da plataforma móvel
    assets[PLATAFORMA_MOVEL_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'plataforma_movel.png')).convert_alpha()
    assets[PLATAFORMA_MOVEL_IMG] = pygame.transform.scale(assets['plataforma_movel_img'], (PLATAFORMA_MOVEL_LARGURA, PLATAFORMA_MOVEL_ALTURA))
        # Carrega chave final
    assets[CHAVE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'key.png')).convert_alpha()
    assets[CHAVE_IMG] = pygame.transform.scale(assets['chave_img'], (CHAVE_LARGURA, CHAVE_ALTURA))
        # Carrega a imagem dos espinhos
    assets[ESPINHO_IMG] = []
        # Sorteia o tamanho dos espinhos que serão sorteados no jogo
    for tamanho in range(50, 131, 10):
        img = pygame.image.load(os.path.join(IMG_DIR, 'espinho2.png')).convert_alpha()
        assets[ESPINHO_IMG].append(pygame.transform.scale(img, (tamanho, tamanho)))

# Carrega as animações do jogo
    # Define animação do dano
    piscando_anim = []
    for i in range(0,8):
        arquivo_anim = os.path.join(IMG_DIR, 'piscando{}.png'.format(i))
        imagem = pygame.image.load(arquivo_anim).convert_alpha()
        imagem = pygame.transform.scale(imagem, (75, 125))
        piscando_anim.append(imagem)
    assets[PISCANDO_ANIM] = piscando_anim

    # Define a animação da tela de vitória
    ganhando_anim = []
    for i in range(1,69):
        arquivo_anim = os.path.join(IMG_DIR, 'Slide{}.PNG'.format(i))
        fundo = pygame.image.load(arquivo_anim)
        fundo= pygame.transform.scale(fundo, (LARGURA, ALTURA))
        ganhando_anim.append(fundo)
    assets[GANHANDO_ANIM] = ganhando_anim

    # Define animmação da morte
    diminuindo_anim = []
    # Configura lista de tamanhos para a animação
    lista_animacao =  [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in lista_animacao:
        arquivo_anim2 = os.path.join(IMG_DIR, 'Peach2.png')
        imagem2 = pygame.image.load(arquivo_anim2).convert_alpha()
        imagem2 = pygame.transform.scale(imagem2, (3*i, 5*i))
        diminuindo_anim.append(imagem2)
    assets[DIMINUINDO_ANIM] = diminuindo_anim

    # Carrega a imagem da vida do jogador
    assets[CORACAO] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
        # Carrega o som da trilha sonora
    assets[TRILHA_SONORA] = pygame.mixer.Sound(os.path.join(SND_DIR, 'trilha_sonora1.wav'))
        # Carrega o som da morte
    assets[SOM_MORTE] = pygame.mixer.Sound(os.path.join(SND_DIR, 'morte.wav'))
        # Carrega o som da personagem ganhando vida
    assets[SOM_COGUMELO] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som_cogumelo.wav'))
        # Carrega o som do dano dos espinhos no jogador
    assets[SOM_DANO] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som_dano.wav'))
        # Carrega o som do espinho gigante
    assets[SOM_ESPINHO_GIGANTE] = pygame.mixer.Sound(os.path.join(SND_DIR, 'Boss_fight2.wav'))
        # Carrega o som da tela de gameover
    assets[SOM_TELA_GAMEOVER] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som_tela_gameover.wav'))
        # Carrega o som da tela de vitória
    assets[SOM_VITORIA] = pygame.mixer.Sound(os.path.join(SND_DIR, 'som_vitoria.wav'))
    return assets 