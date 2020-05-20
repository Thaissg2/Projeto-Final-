import random
import pygame
from Configuração import ESPINHO_LARGURA, ESPINHO_ALTURA, PLATAFORMA_LARGURA, PLATAFORMA_ALTURA, PEACH_LARGURA, PEACH_ALTURA, BLOCO_TAMANHO, COGUMELO_ALTURA, COGUMELO_LARGURA, GIGANTE_ALTURA, GIGANTE_LARGURA, IMG_DIR, SND_DIR, FNT_DIR, PARADO, PULANDO, CAINDO, GRAVIDADE, PULO, VELOCIDADE_X, BLOCO, VAZIO, VELOCIDADE_FUNDO, MAPA
from Assets import FUNDO, ESPINHO_IMG, PLATAFORMA_IMG, PEACH_IMG, BLOCO_IMG, COGUMELO_IMG, ESPINHO_GIGANTE_IMG, TRILHA_SONORA, SOM_MORTE, SOM_COGUMELO, SOM_DANO


# Classe dos blocos
class Blocos(pygame.sprite.Sprite):
    def __init__(self, bloco_img, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem do bloco.
        self.image = bloco_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        # Posiciona o bloco
        self.rect.x = BLOCO_TAMANHO * coluna
        self.rect.y = BLOCO_TAMANHO * linha

# Classe do jogador
class Peach(pygame.sprite.Sprite):
    def __init__(self, peach_img, linha, coluna, blocos):
        pygame.sprite.Sprite.__init__(self)
        # Define o estado atual do jogador
        self.state = PARADO
        # Define a imagem do jogador
        self.image = peach_img
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhe sobre o posicionamento
        self.rect = self.image.get_rect()
        # Guarda o grupo de blocos
        self.blocks = blocos
        # Posiciona o personagem
        self.rect.x = coluna * BLOCO_TAMANHO
        self.rect.centerx = LARGURA/2
        self.rect.bottom = linha * BLOCO_TAMANHO
        self.velocidadex = 0
        self.velocidadey = 0

    def update(self):
        # Atualização da posição do jogador no eixo y
        self.velocidadey += GRAVIDADE
        if self.velocidadey > 0:
            self.state = CAINDO
        # Atualiza posição y
        self.rect.y += self.velocidadey
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do jogador para antes da colisão
        for colisão in colisões:
            if self.velocidadey > 0:
                self.rect.bottom = colisão.rect.top
                # Se colidiu com algo para de cair
                self.velocidadey = 0
                # Atualiza a posição para parado
                self.state = PARADO
            elif self.velocidadey < 0:
                self.rect.top = colisão.rect.top
                # Se colidiu com algo para de cair
                self.velocidadey = 0
                # Atualiza a posição para parado
                self.state = PARADO
        # Atualização da posição do jogador no eixo x
        self.rect.x += self.velocidadex
        # Corrige a posição caso tenha passado o tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA - 1
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do jogador para antes da colisão
        for colisão in colisões:
            if self.velocidadex > 0:
                self.rect.right = colisão.rect.left
            elif self.velocidadex < 0:
                self.rect.left = colisão.rect.right
    
    # Definindo o pulo do jogador
    def jump (self):
        if self.state == PARADO:
            self.velocidadey -= PULO
            self.state = PULANDO

# Classe do espinho
class Espinho(pygame.sprite.Sprite):
    def __init__(self, espinho_img, blocos):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem do espinho
        self.image = espinho_img
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhe sobre o posicionamento
        self.rect = self.image.get_rect()
        # Posiciona espinho
        self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
        self.rect.y = random.randint(-100, -ESPINHO_ALTURA)
        self.velocidadex = random.choice([-5,-4,-3,3,4,5])
        self.velocidadey = 6
        self.blocks = blocos

    def update(self):
        # Atualizando a posição do espinho
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se o espinho passar do final da tela, volta para cima e sorteia novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            # Sorteio novo do tamanho
            ESPINHO_ALTURA = random.randint(50,130)
            ESPINHO_LARGURA = ESPINHO_ALTURA
            # Recarrega as imagens com o novo tamanho
            espinho_img = pygame.image.load('assets/espinho2.png').convert_alpha()
            espinho_img = pygame.transform.scale(espinho_img, (ESPINHO_LARGURA, ESPINHO_ALTURA))
            # Define a imagem do espinho
            self.image = espinho_img
            self.mask = pygame.mask.from_surface(self.image)
            # Posiciona o espinho no jogo
            self.rect = self.image.get_rect()
            # Sorteia novamente as posições dos espinhos novos
            self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
            self.rect.y = random.randint(-200, -ESPINHO_ALTURA)
            self.velocidadex = random.choice([-5,-4,-3,3,4,5])
            self.velocidadey = 8
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do espinho antes da colisão
        for colisão in colisões:
            self.velocidadey = 0

# Classe do espinho gigante
class EspinhoGigante(pygame.sprite.Sprite):
    def __init__(self, espinho_gigante_img, blocos):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem da classe
        self.image = espinho_gigante_img
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhe sobre o posicionamento
        self.rect = self.image.get_rect()
        # Posiciona o espinho gigante
        self.rect.x = 0
        self.rect.bottom = 0
        self.velocidadex = 0
        self.velocidadey = 5
        # Guarda o grupos de blocos
        self.blocks = blocos

    def update(self):
        # Atualizando a posição do espinho gigante
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do espinho antes da colisão
        for colisão in colisões:
            self.velocidadey = 0 
            if self.velocidadex == 0:
                self.velocidadex = 5

# Classe da Plataforma Móvel
class PlataformaMóvel(pygame.sprite.Sprite):
    def __init__(self, espinho_gigante_img, blocos):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem da classe
        self.image = bloco_img
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()
        # Posiciona a plataforma
        self.rect.x = LARGURA/2
        self.rect.bottom = 0
        self.velocidadex = 0
        self.velocidadey = 2
        # Guarda o grupo de blocos
        self.blocks = blocos
        
    def update(self):
        # Atualizando a posição da plataforma móvel
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey

# Classe que representa contato da Peach com espinho
class Contato(pygame.sprite.Sprite):
    def __init__(self, center, piscando_anim):
        pygame.sprite.Sprite.__init__(self)
        # Armazena a animação de explosão
        self.piscando_anim = piscando_anim
        # Inicia o processo de animação colocando a primeira imagem na tela.
        # Armazena o índice atual na animação
        self.frame = 0
        # Pega a primeira imagem
        self.image = self.piscando_anim[self.frame]
        self.rect = self.image.get_rect()
        # Posiciona o centro da imagem
        self.rect.center = center
        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos
        self.frame_ticks = 50
        
        def update(self):
            # Verifica o tick atual.
            atual = pygame.time.get_ticks()
            # Verifica quantos ticks se passaram desde a ultima mudança de frame.
            elapsed_ticks = atual - self.last_update
            # Se já está na hora de mudar de imagem...
            if elapsed_ticks > self.frame_ticks:
                # Marca o tick da nova imagem.
                self.last_update = atual
                # Avança um quadro.
                self.frame += 1
                # Verifica se já chegou no final da animação.
            if self.frame == len(self.piscando_anim):
                # Se sim, tchau piscando!
                self.kill()
            else:
                # Se ainda não chegou ao fim da piscada, troca de imagem.
                center = self.rect.center
                self.image = self.piscando_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Classe do Cogumelo
class Cogumelo(pygame.sprite.Sprite):
    def __init__(self, cogumelo_img, blocos):
        pygame.sprite.Sprite.__init__(self)
        # Armazena a imagem do cogumelo
        self.image = cogumelo_img
        self.mask = pygame.mask.from_surface(self.image)
        # Define a posição do cogumelo
        self.rect = self.image.get_rect()
        # Posiciona o cogumelo
        self.rect.x = random.randint(0, LARGURA-COGUMELO_LARGURA)
        self.rect.y = random.randint(-100, -COGUMELO_ALTURA)
        self.velocidadex = 0
        self.velocidadey = 6
        self.blocks = blocos

    def update(self):
        # Atualizando a posição do cogumelo
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do espinho antes da colisão
        for colisão in colisões:
            self.velocidadey = 0 
            if self.velocidadex == 0:
                self.velocidadex = random.choice([-5,-4, 4, 5])           

# Classe da plataforma fixa
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, plataforma_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = plataforma_img
        self.rect = self.image.get_rect()
        self.rect.bottom = ALTURA