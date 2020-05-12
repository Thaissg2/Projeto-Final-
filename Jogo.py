# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()
 
# ----- Gera tela principal
LARGURA = 480
ALTURA = 600
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Super Maria Sis')
 
# ----- Inicia assets
ESPINHO_LARGURA = 50
ESPINHO_ALTURA = 38
PLATAFORMA_LARGURA = 480
PLATAFORMA_ALTURA = 40
PEACH_LARGURA = 75
PEACH_ALTURA = 125
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('assets/fundo2.png').convert()
espinho_img = pygame.image.load('assets/espinho.png').convert_alpha()
espinho_img = pygame.transform.scale(espinho_img, (ESPINHO_LARGURA, ESPINHO_ALTURA))
plataforma_img = pygame.image.load('assets/plataforma.png').convert_alpha()
plataforma_img = pygame.transform.scale(plataforma_img, (PLATAFORMA_LARGURA, PLATAFORMA_ALTURA))
peach_img = pygame.image.load('assets/peach.png').convert_alpha()
peach_img= pygame.transform.scale(peach_img, (PEACH_LARGURA, PEACH_ALTURA))

 
# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Peach(pygame.sprite.Sprite):
    def __init__(self, img):
    # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA/2
        self.rect.bottom = ALTURA - 45
        self.velocidadex = 0

    def update(self):
        #Atualização da posição da Peach
        self.rect.x += self.velocidadex
        #Mantém a Peach dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rec.left = 0

class Espinho(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
        self.rect.y = random.randint(-100, -ESPINHO_ALTURA)
        self.velocidadex = random.randint(-3, 3)
        self.velocidadey = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do espinho
        self.rect.x += self.velocidadex
        self.rect.y += self.velocidadey
        # Se o espinho passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
            self.rect.y = random.randint(-100, -ESPINHO_ALTURA)
            self.velocidadex = random.randint(-3, 3)
            self.velocidadey = random.randint(2, 9)

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.bottom = ALTURA - 10

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando os espinhos
todos_espinhos = pygame.sprite.Group()
for i in range(6):
    espinho = Espinho(espinho_img)
    todos_espinhos.add(espinho)

plataforma = Plataforma(plataforma_img)

#Criando o jogador
jogador = Peach(peach_img)
todos_espinhos.add(jogador)


# ===== Loop principal =====
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
                jogador.velocidadex -= 8
            if event.key == pygame.K_RIGHT:
                jogador.velocidadex += 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                jogador.velocidadex += 8
            if event.key == pygame.K_RIGHT:
                jogador.velocidadex -= 8
    # ----- Atualiza estado do jogo
    # Atualizando a posição dos espinhos
    todos_espinhos.update()
    # ----- Gera saídas

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))

    # Desenhando espinhos
    todos_espinhos.draw(window)
    window.blit(plataforma.image, plataforma.rect)
    #window.blit(peach.image, peach.rect)
    pygame.display.update()

 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados