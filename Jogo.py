# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from os import path
import time

pygame.init()
pygame.mixer.init()
 
# ----- Gera tela principal
LARGURA = 880
ALTURA = 600
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Super Maria Sis')
# Variável para o ajuste de velocidade
FPS = 30

# ----- Inicia assets
ESPINHO_LARGURA = 50
ESPINHO_ALTURA = 50
PLATAFORMA_LARGURA = LARGURA
PLATAFORMA_ALTURA = 40
PEACH_LARGURA = 75
PEACH_ALTURA = 125
BLOCO_TAMANHO = 40
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('assets/fundo2.jpg').convert_alpha()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
espinho_img = pygame.image.load('assets/espinho2.png').convert_alpha()
espinho_img = pygame.transform.scale(espinho_img, (ESPINHO_LARGURA, ESPINHO_ALTURA))
plataforma_img = pygame.image.load('assets/plataforma.png').convert_alpha()
plataforma_img = pygame.transform.scale(plataforma_img, (PLATAFORMA_LARGURA, PLATAFORMA_ALTURA))
peach_img = pygame.image.load('assets/Peach2.png').convert_alpha()
peach_img= pygame.transform.scale(peach_img, (PEACH_LARGURA, PEACH_ALTURA))
bloco_img =  pygame.image.load('assets/bloco.jpg').convert_alpha()
bloco_img = pygame.transform.scale(bloco_img, (BLOCO_TAMANHO, BLOCO_TAMANHO))

# Carrega os sons do jogo
trilha_sonora = pygame.mixer.Sound('assets/trilha_sonora.wav')
#trilha_sonora = pygame.mixer.music.set_volume(1)

som_morte = pygame.mixer.Sound('assets/morte.wav')

# Define a aceleração da gravidade
GRAVIDADE = 5
# Define a velocidade inicial no pulo
PULO = 45
# Define a velocidade em x
VELOCIDADE_X = 9

# Definindo tipos de blocos
BLOCO = 0
VAZIO = -1 

# Definindo velocidade do fundo
VELOCIDADE_FUNDO = -2

# Criando o mapa
MAPA = [
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
    [BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO, BLOCO],
    [VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
]

# Define estado do jogador
PARADO = 0
PULANDO = 1
CAINDO = 2

# Definindo blocos
class Blocos(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, bloco_img, linha, coluna):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem do tile.
        self.image = bloco_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        # Posiciona o tile
        self.rect.x = BLOCO_TAMANHO * coluna
        self.rect.y = BLOCO_TAMANHO * linha 

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Peach(pygame.sprite.Sprite):
    def __init__(self, peach_img, linha, coluna, blocos):
    # Construtor da classe py (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Define o estato atual do jogador
        self.state = PARADO
        # Define a imagem do Sprite
        self.image = peach_img
        self.mask = pygame.mask.from_surface(self.image)
        # Detalhe sobre o posicionamento
        self.rect = self.image.get_rect()
        # Guarda o grupo de blocos
        self.blocks = blocos
        # Posiciona o personagem
        self.rect.x = coluna * BLOCO_TAMANHO
        #self.rect.centerx = LARGURA/2
        self.rect.bottom = linha * BLOCO_TAMANHO
        self.velocidadex = 0
        self.velocidadey = 0

    def update(self):
        #Atualização da posição da Peach
        #No eixo y
        self.velocidadey += GRAVIDADE
        if self.velocidadey > 0:
            self.state = CAINDO
        #Atualiza posição y
        self.rect.y += self.velocidadey
        #Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        #Corrige a posição do personagem para antes da colisão
        for colisão in colisões:
            if self.velocidadey > 0:
                self.rect.bottom = colisão.rect.top
                #Se colidiu com algo para de cair
                self.velocidadey = 0
                #Atualiza a posição para parado
                self.state = PARADO
            elif self.velocidadey < 0:
                self.rect.top = colisão.rect.top
                #Se colidiu com algo para de cair
                self.velocidadey = 0
                #Atualiza a posição para parado
                self.state = PARADO
        #No eixo x
        self.rect.x += self.velocidadex
        #Corrige a posição caso tenha passado o tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA - 1
        #Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        #Corrige a posição do personagem para antes da colisão
        for colisão in colisões:
            if self.velocidadex > 0:
                self.rect.right = colisão.rect.left
            elif self.velocidadex < 0:
                self.rect.left = colisão.rect.right
    
    #Método que faz o personagem pular
    def jump (self):
        if self.state == PARADO:
            self.velocidadey -= PULO
            self.state = PULANDO
    

class Espinho(pygame.sprite.Sprite):
    def __init__(self, espinho_img, blocos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = espinho_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
        self.rect.y = random.randint(-100, -ESPINHO_ALTURA)
        self.velocidadex = random.choice([-5,-4,-3,3,4,5])
        self.velocidadey = 6
        self.blocks = blocos


    def update(self):
        # Atualizando a posição do espinho
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se o espinho passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            ESPINHO_ALTURA = random.randint(50,130)
            ESPINHO_LARGURA = ESPINHO_ALTURA
            espinho_img = pygame.image.load('assets/espinho2.png').convert_alpha()
            espinho_img = pygame.transform.scale(espinho_img, (ESPINHO_LARGURA, ESPINHO_ALTURA))
            self.image = espinho_img
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
            self.rect.y = random.randint(-200, -ESPINHO_ALTURA)
            self.velocidadex = random.choice([-5,-4,-3,3,4,5])
            self.velocidadey = 8

        #Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        #Corrige a posição do espinho antes da colisão
        for colisão in colisões:
            self.velocidadey = 0

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.bottom = ALTURA

def game_screen(window):
    clock = pygame.time.Clock()
    todos_sprites = pygame.sprite.Group()
    todos_espinhos = pygame.sprite.Group()
    blocos = pygame.sprite.Group()

    #Carregando fundo do jogo
    fundo_rect = fundo.get_rect()

    # Criando o jogador
    jogador = Peach(peach_img, 14, 0, blocos)
    # Cria blocos de acordo com o mapa
    for linha in range(len(MAPA)):
        for coluna in range(len(MAPA[linha])):
            tipo_bloco = MAPA[linha][coluna]
            if tipo_bloco == BLOCO:
                tile = Blocos(bloco_img, linha, coluna)
                todos_sprites.add(tile)
                blocos.add(tile)
    # Adiciona o jogador por cima dos blocos
    todos_sprites.add(jogador)
    
    # Criando os espinhos
    for i in range(4):
        espinho= Espinho(espinho_img, blocos)
        todos_sprites.add(espinho)
        todos_espinhos.add(espinho)

    plataforma = Plataforma(plataforma_img)
    blocos.add(plataforma)

    # ===== Loop principal =====
    game = True

    trilha_sonora.play()

    while game:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            # ---- Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    jogador.velocidadex -= VELOCIDADE_X
                if event.key == pygame.K_RIGHT:
                    jogador.velocidadex += VELOCIDADE_X
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    jogador.jump()
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    jogador.velocidadex += VELOCIDADE_X
                if event.key == pygame.K_RIGHT:
                    jogador.velocidadex -= VELOCIDADE_X

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos espinhos
        todos_sprites.update()

        #Atualiza posicao da imagem de fundo
        fundo_rect.y -= VELOCIDADE_FUNDO

        #Verifica se o fundo saiu para baixo
        if fundo_rect.top > ALTURA:
            fundo_rect.y -= fundo_rect.height

        #---- Verifica se houve dano entre Peach e Espinho
        dano = pygame.sprite.spritecollide(jogador, todos_espinhos, True,  pygame.sprite.collide_mask)
        if len(dano) > 0:
            trilha_sonora.stop()
            som_morte.play()
            #Tempo antes de fechar o jogo
            time.sleep(2.3)
            game = False


        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca

        #Alem disso, deve ser cíclica, ou seja, a parte de cima deve ser continuacao da parte de baixo
        window.blit(fundo, fundo_rect)

        #Desenha o fundo com cópia pra cima
        fundo_rect2 = fundo_rect.copy()
        if fundo_rect.top > 0:
            fundo_rect2.y -= fundo_rect2.height
        window.blit(fundo, fundo_rect2)
       

        # Desenhando espinhos
        todos_sprites.draw(window)
        window.blit(plataforma.image, plataforma.rect)
        #window.blit(peach.image, peach.rect)
        pygame.display.update()

game_screen(window)
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados