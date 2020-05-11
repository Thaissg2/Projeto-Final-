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
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('assets/fundo.jpg').convert()
espinho_img = pygame.image.load('assets/espinho.png').convert_alpha()
espinho_img = pygame.transform.scale(espinho_img, (ESPINHO_LARGURA, ESPINHO_ALTURA))
 
# ----- Inicia estruturas de dados
# Definindo os novos tipos
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
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA or self.rect.right < 0 or self.rect.left > LARGURA:
            self.rect.x = random.randint(0, LARGURA-ESPINHO_LARGURA)
            self.rect.y = random.randint(-100, -ESPINHO_ALTURA)
            self.velocidadex = random.randint(-3, 3)
            self.velocidadey = random.randint(2, 9)


game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30


# Criando os espinhos
todos_espinhos = pygame.sprite.Group()
for i in range(6):
    espinho = Espinho(espinho_img)
    todos_espinhos.add(espinho)
 
# ===== Loop principal =====
while game:
    clock.tick(FPS)
 
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
 
    # ----- Atualiza estado do jogo
    # Atualizando a posição dos espinhos
    todos_espinhos.update()
    # ----- Gera saídas

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))

    # Desenhando espinhos
    todos_espinhos.draw(window)
    pygame.display.update()

 
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados