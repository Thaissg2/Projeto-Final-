import random
import pygame
from Configuracao import *
from Assets import *


# Classe dos blocos
class Blocos(pygame.sprite.Sprite):
    def __init__(self, grupos, assets, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem do bloco.
        self.image = assets[BLOCO_IMG]
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        # Posiciona o bloco
        self.rect.x = BLOCO_TAMANHO * coluna
        self.rect.y = BLOCO_TAMANHO * linha
        self.grupos = grupos
        self.assets = assets
        self.velocidadey = 0

# Classe do jogador
class Peach(pygame.sprite.Sprite):
    def __init__(self, grupos, assets, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        # Define o estado atual do jogador
        self.state = PARADO
        # Define a imagem do jogador
        self.image = assets[PEACH_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhe sobre o posicionamento
        self.rect = self.image.get_rect()
        # Guarda o grupo de blocos
        self.grupos = grupos
        self.blocos = grupos['blocos']
        # Posiciona o personagem
        self.rect.x = coluna * BLOCO_TAMANHO
        self.rect.centerx = LARGURA/2
        self.rect.bottom = linha * BLOCO_TAMANHO
        self.velocidadex = 0
        self.velocidadey = 0
        self.assets = assets

    def update(self):
        # Atualização da posição do jogador no eixo y
        self.velocidadey += GRAVIDADE
        if self.velocidadey > 0:
            self.state = CAINDO
        # Atualiza posição y
        self.rect.y += self.velocidadey
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocos, False)
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
        colisões = pygame.sprite.spritecollide(self, self.blocos, False)
        # Corrige a posição do jogador para antes da colisão
        for colisão in colisões:
            if self.velocidadex > 0:
                self.rect.right = colisão.rect.left
            elif self.velocidadex < 0:
                self.rect.left = colisão.rect.right
                
    def jump (self):
        if self.state == PARADO:
            self.velocidadey -= PULO
            self.state = PULANDO

# Classe do espinho
class Espinho(pygame.sprite.Sprite):
    def __init__(self, assets, grupos):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem do espinho
        self.orig_image = assets[ESPINHO_IMG]
        self.image = assets[ESPINHO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhe sobre o posicionamento
        self.rect = self.image.get_rect()
        # Posiciona espinho
        self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
        self.rect.y = random.randint(-100, -ESPINHO_ALTURA)
        self.velocidadex = random.choice([-5,-4,-3,3,4,5])
        self.velocidadey = 6
        self.assets = assets
        self.grupos = grupos
        self.blocos = self.grupos['blocos']
        if self.velocidadex > 0:
            self.rot_velocidade = -10
        else:
            self.rot_velocidade = 10
        self.rot = 0

    def update(self):
        # Atualizando a posição do espinho
        center = self.rect.center
        self.rot = (self.rot + self.rot_velocidade) % 360
        self.image = pygame.transform.rotate(self.orig_image, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se o espinho passar do final da tela, volta para cima e sorteia novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            # Sorteio novo do tamanho
            ESPINHO_ALTURA = random.randint(50,130)
            ESPINHO_LARGURA = ESPINHO_ALTURA
            # Recarrega as imagens com o novo tamanho
            self.assets[ESPINHO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'espinho2.png')).convert_alpha()
            self.assets[ESPINHO_IMG] = pygame.transform.scale(self.assets['espinho_img'], (ESPINHO_LARGURA, ESPINHO_ALTURA))
            # Define a imagem do espinho
            self.image = self.assets[ESPINHO_IMG]
            self.mask = pygame.mask.from_surface(self.image)
            # Posiciona o espinho no jogo
            self.rect = self.image.get_rect()
            # Sorteia novamente as posições dos espinhos novos
            self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
            self.rect.y = random.randint(-200, -ESPINHO_ALTURA)
            self.velocidadex = random.choice([-5,-4,-3,3,4,5])
            self.velocidadey = 8
            if self.velocidadex > 0:
                self.rot_velocidade = -10
            else:
                self.rot_velocidade = 10
        # Corrige a posição do espinho antes da colisão
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocos, False)
        # Corrige a posição do espinho antes da colisão
        # Se colidiu com algum bloco, volta para o ponto anterior
        for colisão in colisões:
            self.velocidadey = colisão.velocidadey
        if len(colisões) == 0:
            self.velocidadey = 8


# Classe do espinho gigante
class EspinhoGigante(pygame.sprite.Sprite):
    def __init__(self, assets, grupos):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem da classe
        self.image = assets[ESPINHO_GIGANTE_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhe sobre o posicionamento
        self.rect = self.image.get_rect()
        # Posiciona o espinho gigante
        self.rect.x = 0
        self.rect.bottom = 0
        self.velocidadex = 0
        self.velocidadey = 5
        # Guarda o grupos de blocos
        self.blocos = grupos['blocos']
        self.grupos = grupos
        self.assets = assets
        
    def update(self):
        # Atualizando a posição do espinho gigante
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocos, False)
        # Corrige a posição do espinho antes da colisão
        for colisão in colisões:
            self.velocidadey = 0 
            if self.velocidadex == 0:
                self.velocidadex = 5

# Classe da Plataforma Móvel
class PlataformaMóvel(pygame.sprite.Sprite):
    def __init__(self, assets, grupos):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem da classe
        self.image = assets[PLATAFORMA_MOVEL_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()
        # Posiciona a plataforma
        self.rect.centerx = LARGURA/2
        self.rect.bottom = 0
        self.velocidadex = 0
        self.velocidadey = 2
        # Guarda o grupo de blocos
        self.grupos = grupos
        self.blocos = grupos['blocos']
        self.assets = assets
        
    def update(self):
        # Atualizando a posição da plataforma móvel
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey

# Classe que representa contato da Peach com espinho
class Contato(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        pygame.sprite.Sprite.__init__(self)
        # Armazena a animação de explosão
        self.piscando_anim = assets[PISCANDO_ANIM]
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
        # Verifica quantos ticks se passaram desde a ultima mudança de frame
        elapsed_ticks = atual - self.last_update
        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem
            self.last_update = atual
            # Avança um quadro
            self.frame += 1
            # Verifica se já chegou no final da animação
        if self.frame == len(self.piscando_anim):
            # Se sim, finaliza a animação
            self.kill()
        else:
            # Se ainda não chegou ao fim da lista, troca de imagem
            center = self.rect.center
            self.image = self.piscando_anim[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center

# Classe que representa animação de fim de jogo
class GameOver(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Armazena a animação da morte
        self.diminuindo_anim = assets[DIMINUINDO_ANIM]
        # Inicia o processo de animação colocando a primeira imagem na tela
        # Armazena o índice atual na animação
        self.frame = 0 
        # Pega a primeira imagem
        self.image = self.diminuindo_anim[self.frame]
        self.rect = self.image.get_rect()
        # Posiciona o centro da imagem
        self.rect.center = center  
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a próxima imagem da animação será mostrada
        self.frame_ticks = 101

    def update(self):
    # Verifica o tick atual.
        atual = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame
        elapsed_ticks = atual - self.last_update
        # Se já está na hora de mudar de imagem
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem
            self.last_update = atual
            # Avança um quadro
            self.frame += 1
            # Verifica se já chegou no final da animação
            if self.frame == len(self.diminuindo_anim):
                # Se sim, finaliza a animação de game over
                self.kill()
            else:
                # Se ainda não chegou ao fim da lista, troca de imagem
                center = self.rect.center
                self.image = self.diminuindo_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    

# Classe do Cogumelo
class Cogumelo(pygame.sprite.Sprite):
    def __init__(self, assets, grupos):
        pygame.sprite.Sprite.__init__(self)
        # Armazena a imagem do cogumelo
        self.image = assets[COGUMELO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        # Define a posição do cogumelo
        self.rect = self.image.get_rect()
        # Posiciona o cogumelo
        self.rect.x = random.randint(0, LARGURA-COGUMELO_LARGURA)
        self.rect.y = random.randint(-100, -COGUMELO_ALTURA)
        self.velocidadex = 0
        self.velocidadey = 6
        # Guarda o grupo de blocos
        self.grupos = grupos
        self.blocos = grupos['blocos']
        self.assets = assets

    def update(self):
        # Atualizando a posição do cogumelo
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocos, False)
        # Corrige a posição do espinho antes da colisão
        for colisão in colisões:
            self.velocidadey = colisão.velocidadey 
            if self.velocidadex == 0:
                self.velocidadex = random.choice([-5,-4, 4, 5]) 
        if len(colisões) == 0:
            self.velocidadey = 6          

# Classe da plataforma fixa
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[PLATAFORMA_IMG]
        self.rect = self.image.get_rect()
        self.rect.bottom = ALTURA
        self.assets = assets
        self.velocidadey = 0