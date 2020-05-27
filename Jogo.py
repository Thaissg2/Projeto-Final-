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
pygame.display.set_caption('New Super Peach Sis')
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
COGUMELO_ALTURA = 35
COGUMELO_LARGURA = 35
GIGANTE_ALTURA = 200
GIGANTE_LARGURA = 200

font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('assets/fundo2.jpg').convert_alpha()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
espinho_img = pygame.image.load('assets/espinho2.png').convert_alpha()
espinho_img = pygame.transform.scale(espinho_img, (ESPINHO_LARGURA, ESPINHO_ALTURA))
plataforma_img = pygame.image.load('assets/plataforma.png').convert_alpha()
plataforma_img = pygame.transform.scale(plataforma_img, (PLATAFORMA_LARGURA, PLATAFORMA_ALTURA))
peach_img = pygame.image.load('assets/Peach2.png').convert_alpha()
peach_img= pygame.transform.scale(peach_img, (PEACH_LARGURA, PEACH_ALTURA))
bloco_img =  pygame.image.load('assets/plataforma_movel.png').convert_alpha()
bloco_img = pygame.transform.scale(bloco_img, (150, BLOCO_TAMANHO))
cogumelo_img = pygame.image.load('assets/cogumelo.png').convert_alpha()
cogumelo_img = pygame.transform.scale(cogumelo_img, (COGUMELO_LARGURA, COGUMELO_ALTURA))
espinho_gigante_img = pygame.image.load('assets/espinho2.png').convert_alpha()
espinho_gigante_img = pygame.transform.scale(espinho_gigante_img, (GIGANTE_LARGURA, GIGANTE_ALTURA))

coracao = pygame.font.Font('assets/PressStart2P.ttf', 28)
piscando_anim = []
diminuindo_anim = []

for i in range(0,8):
    # Definindo animmação do dano
    arquivo_anim = 'assets/piscando{}.png'.format(i)
    img = pygame.image.load(arquivo_anim).convert_alpha()
    img = pygame.transform.scale(img, (75, 125))
    piscando_anim.append(img)


lista_animacao =  [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in lista_animacao:
     # Definindo animação da morte'
      img2 = pygame.image.load('assets/Peach2.png').convert_alpha()
      img2 = pygame.transform.scale(img2, (3*i, 5*i))
      diminuindo_anim.append(img2)

# Carrega os sons do jogo
trilha_sonora = pygame.mixer.Sound('assets/trilha_sonora1.wav')
som_morte = pygame.mixer.Sound('assets/morte.wav')
som_cogumelo = pygame.mixer.Sound('assets/som_cogumelo.wav')
som_dano = pygame.mixer.Sound('assets/som_dano.wav')

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
        # Posiciona a personagem
        self.rect.x = coluna * BLOCO_TAMANHO
        self.rect.centerx = LARGURA/2
        self.rect.bottom = linha * BLOCO_TAMANHO
        self.velocidadex = 0
        self.velocidadey = 0

    def update(self):
        # Atualização da posição da Peach
        # No eixo y
        self.velocidadey += GRAVIDADE
        if self.velocidadey > 0:
            self.state = CAINDO
        # Atualiza posição y
        self.rect.y += self.velocidadey
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
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
        # No eixo x
        self.rect.x += self.velocidadex
        # Corrige a posição caso tenha passado o tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA - 1
        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for colisão in colisões:
            if self.velocidadex > 0:
                self.rect.right = colisão.rect.left
            elif self.velocidadex < 0:
                self.rect.left = colisão.rect.right
    
    # Método que faz o personagem pular
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
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
            self.rect.y = random.randint(-200, -ESPINHO_ALTURA)
            self.velocidadex = random.choice([-5,-4,-3,3,4,5])
            self.velocidadey = 8

        # Se colidiu com algum bloco, volta para o ponto anterior
        colisões = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do espinho antes da colisão
        for colisão in colisões:
            if self.velocidadex > 0:
                self.rect.right = colisão.rect.left
            elif self.velocidadex < 0:
                self.rect.left = colisão.rect.right

# Costruindo classe do espinho gigante
class EspinhoGigante(pygame.sprite.Sprite):
    def __init__(self, espinho_gigante_img, blocos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = espinho_gigante_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.bottom = 0
        self.velocidadex = 0
        self.velocidadey = 5
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

# Construindo classe da Plataforma Móvel
class PlataformaMóvel(pygame.sprite.Sprite):
    def __init__(self, espinho_gigante_img, blocos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = bloco_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = LARGURA/2
        self.rect.bottom = 0
        self.velocidadex = 0
        self.velocidadey = 2
        self.blocks = blocos


    def update(self):
        # Atualizando a posição da plataforma móvel
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey


# Classe que representa contato da Peach com espinho
class Contato(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, piscando_anim):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        # Armazena a animação da morte
        self.piscando_anim = piscando_anim
 
        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.piscando_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem
 
        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()
 
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
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

# Classe que representa contato da Peach com espinho
class GameOver(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, diminuindo_anim):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        # Armazena a animação da morte
        self.diminuindo_anim = diminuindo_anim
 
        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.diminuindo_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem
 
        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()
 
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 101
 
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
            if self.frame == len(self.diminuindo_anim):
                # Se sim, tchau diminuindi!
                self.kill()
            else:
                # Se ainda não chegou ao fim da piscada, troca de imagem.
                center = self.rect.center
                self.image = self.diminuindo_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Classe cogumelo
class Cogumelo(pygame.sprite.Sprite):
    def __init__(self, cogumelo_img, blocos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = cogumelo_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
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


# Classe que representa a plataforma
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
    todos_cogumelos = pygame.sprite.Group()
    todos_espinhos_gigantes = pygame.sprite.Group()
    blocos = pygame.sprite.Group()

    # Carregando fundo do jogo
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
    for i in range(1):
        espinho= Espinho(espinho_img, blocos)
        todos_sprites.add(espinho)
        todos_espinhos.add(espinho)

    # Criando os cogumelos
    for i in range(1):
        cogumelo = Cogumelo(cogumelo_img, blocos)
        todos_sprites.add(cogumelo)
        todos_cogumelos.add(cogumelo)


    plataforma = Plataforma(plataforma_img)
    blocos.add(plataforma)

    FINAL = 0
    JOGANDO = 1
    MORRENDO = 2
    estado = JOGANDO


    vidas = 3
    keys_down = {}

    # ===== Loop principal =====
    #tela_jogo = pygame.time.get_ticks()
    ultimo_cogumelo = pygame.time.get_ticks()
    espinho_gigante = pygame.time.get_ticks()
    ultima_plataforma = pygame.time.get_ticks()
    comeco_jogo = pygame.time.get_ticks()
    trilha_sonora.play()

    while estado != FINAL:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                estado = FINAL
            # ---- Verifica se apertou alguma tecla.
            if estado == JOGANDO:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        jogador.velocidadex -= VELOCIDADE_X
                    if event.key == pygame.K_RIGHT:
                        jogador.velocidadex += VELOCIDADE_X
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        jogador.jump()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            jogador.velocidadex += VELOCIDADE_X
                        if event.key == pygame.K_RIGHT:
                            jogador.velocidadex -= VELOCIDADE_X

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos espinhos
        todos_sprites.update()

        # Atualiza posicao da imagem de fundo
        fundo_rect.y -= VELOCIDADE_FUNDO

        # Verifica se o fundo saiu para baixo
        if fundo_rect.top > ALTURA:
            fundo_rect.y -= fundo_rect.height

        # ---- Verifica se houve dano entre Peach e Espinho
        if estado == JOGANDO:
            atual = pygame.time.get_ticks()
            if atual - ultimo_cogumelo > 45000:
                ultimo_cogumelo = atual
                c = Cogumelo(cogumelo_img, blocos)
                todos_sprites.add(c)
                todos_cogumelos.add(c)      

            if atual - espinho_gigante > 60000:
                espinho_gigante = atual
                g = EspinhoGigante(espinho_gigante_img, blocos)
                todos_sprites.add(g)
                todos_espinhos_gigantes.add(g)

            if atual - ultima_plataforma > 10000:
                ultima_plataforma = atual
                p = PlataformaMóvel(bloco_img, blocos)
                todos_sprites.add(p)
                blocos.add(p)

            if atual - comeco_jogo > 1000000:
                estado = FINAL
        

        #if atual - tela_jogo > 10000:
            #estado = MORRENDO

            dano = pygame.sprite.spritecollide(jogador, todos_espinhos, True,  pygame.sprite.collide_mask)
            ganhando_vida = pygame.sprite.spritecollide(jogador, todos_cogumelos, True,  pygame.sprite.collide_mask)
            dano_gigante = pygame.sprite.spritecollide(jogador, todos_espinhos_gigantes, True,  pygame.sprite.collide_mask)
            pisando = pygame.sprite.spritecollide(jogador, blocos, False,  pygame.sprite.collide_mask)

            for esp in dano:
            # O espinho é destruido e precisa ser recriado
                e = Espinho(espinho_img, blocos)
                todos_sprites.add(e)
                todos_espinhos.add(e)  

            if len(dano) > 0:
                jogador.kill()
                vidas -= 1
                estado = MORRENDO
                jogador.kill()
                if vidas == 0:
                    trilha_sonora.stop()
                    som_morte.play()
                    game_over = GameOver(jogador.rect.center, diminuindo_anim)
                    todos_sprites.add(game_over)
                else:
                    estado = JOGANDO
                    jogador = Peach(peach_img, linha, coluna, blocos)
                    todos_sprites.add(jogador)
                    som_dano.play()
                    contato = Contato(jogador.rect.center, piscando_anim)
                    todos_sprites.add(contato)
                    piscando_tick = pygame.time.get_ticks()
                    piscando_duracao = contato.frame_ticks * len(contato.piscando_anim)
                keys_down = {}
               

            if len(ganhando_vida) > 0:
                som_cogumelo.play()
                vidas += 1

            if len(pisando) > 0:
                self.velocidadey = 0


            if len(dano_gigante) > 0:
                jogador.kill()
                vidas -= 1
                estado = MORRENDO
                if vidas == 0:
                    trilha_sonora.stop()
                    som_morte.play()
                    game_over = GameOver(jogador.rect.center, diminuindo_anim)
                    todos_sprites.add(game_over)
                else:
                    estado = JOGANDO
                    jogador = Peach(peach_img, linha, coluna, blocos)
                    todos_sprites.add(jogador)
                    som_dano.play()
                    contato = Contato(jogador.rect.center, piscando_anim)
                    todos_sprites.add(contato)
                    piscando_tick = pygame.time.get_ticks()
                    piscando_duracao = contato.frame_ticks * len(contato.piscando_anim)
                keys_down = {}


        elif estado == MORRENDO:
            # atual = pygame.time.get_ticks()
            # if atual - piscando_tick > piscando_duracao:
            # jogador.kill()
            # if vidas == 0:
            #     trilha_sonora.stop()
            #     som_morte.play()
            #     game_over = GameOver(jogador.rect.center, diminuindo_anim)
            #     todos_sprites.add(game_over)
            #     keys_down = {}
            #     piscando_tick = pygame.time.get_ticks()
            #     piscando_duracao = game_over.frame_ticks * len(game_over.diminuindo_anim)
            #     time.sleep(2.3)
            #     estado = FINAL 
            # else:
            #     estado = JOGANDO
            #     jogador = Peach(peach_img, linha, coluna, blocos)
            #     todos_sprites.add(jogador)
            if not game_over.alive():
                estado = FINAL


        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca

        # Além disso, deve ser cíclica, ou seja, a parte de cima deve ser continuação da parte de baixo
        window.blit(fundo, fundo_rect)

        # Desenha o fundo com cópia pra cima
        fundo_rect2 = fundo_rect.copy()
        if fundo_rect.top > 0:
            fundo_rect2.y -= fundo_rect2.height
        window.blit(fundo, fundo_rect2)
       
        # Desenhando espinhos
        todos_sprites.draw(window)
        window.blit(plataforma.image, plataforma.rect)
        #window.blit(peach.image, peach.rect)

        # Desenhando as vidas
        text_surface = coracao.render(chr(9829) * vidas, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10,10)
        window.blit(text_surface, text_rect)

        pygame.display.update()

game_screen(window)
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados