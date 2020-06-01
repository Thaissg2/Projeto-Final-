import pygame
from Configuracao import *
from Assets import *
from Sprites import *

pygame.init()
window = pygame.display.set_mode((LARGURA, ALTURA))

def game_screen(window):
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()
    
    assets = load_assets()

    # Cria os grupos
    todos_sprites = pygame.sprite.Group()
    todos_espinhos = pygame.sprite.Group()
    todos_cogumelos = pygame.sprite.Group()
    todos_espinhos_gigantes = pygame.sprite.Group()
    blocos = pygame.sprite.Group()
    
    grupos = {}
    grupos['todos_sprites'] = todos_sprites
    grupos['todos_espinhos'] = todos_espinhos
    grupos['todos_cogumelos'] = todos_cogumelos
    grupos['todos_espinhos_gigantes'] = todos_espinhos_gigantes
    grupos['blocos'] = blocos
    
    # Cria fundo do jogo
    fundo_rect = assets[FUNDO].get_rect()
    
    # Cria blocos de acordo com o mapa
    for linha in range(len(MAPA)):
        for coluna in range(len(MAPA[linha])):
            tipo_bloco = MAPA[linha][coluna]
            if tipo_bloco == BLOCO:
                tile = Blocos(grupos, assets, linha, coluna)
                todos_sprites.add(tile)
                blocos.add(tile)
                
    # Cria o jogador
    jogador = Peach(grupos, assets, 14, 0)
    todos_sprites.add(jogador)
    
    # Cria os espinhos
    for i in range(4):
        espinho= Espinho(assets, grupos)
        todos_sprites.add(espinho)
        todos_espinhos.add(espinho)
        
    # Cria os cogumelos
    for i in range(1):
        cogumelo = Cogumelo(assets, grupos)
        todos_sprites.add(cogumelo)
        todos_cogumelos.add(cogumelo)

    # Cria a plataforma
    plataforma = Plataforma(assets)
    blocos.add(plataforma)

    # Cria os estados do jogo
    FINAL = 0
    JOGANDO = 1
    MORRENDO = 2
    PERDENDO_VIDAS = 3
    estado = JOGANDO

    # Cria as vidas do jogador
    vidas = 3
    keys_down = {}

    # ===== Loop principal =====
    ultimo_cogumelo = pygame.time.get_ticks()
    espinho_gigante = pygame.time.get_ticks()
    ultima_plataforma = pygame.time.get_ticks()
    comeco_jogo = pygame.time.get_ticks()

    assets[TRILHA_SONORA].play()

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
        # Atualiza a posição dos espinhos
        todos_sprites.update()
        
        # Atualiza posicao da imagem de fundo
        fundo_rect.y -= VELOCIDADE_FUNDO
        
        # Verifica se o fundo saiu para baixo
        if fundo_rect.top > ALTURA:
            fundo_rect.y -= fundo_rect.height
        
        # ---- Verifica se houve contato da Peach com o cogumelo ou espinho
        if estado == JOGANDO:
            atual = pygame.time.get_ticks()
            # Recria o cogumelo após 45 segundos
            if atual - ultimo_cogumelo > 45000:
                ultimo_cogumelo = atual
                c = Cogumelo(assets[COGUMELO_IMG], blocos)
                todos_sprites.add(c)
                todos_cogumelos.add(c)      

            # Recria o cogumelo após 60 segundos
            if atual - espinho_gigante > 60000:
                assets[SOM_ESPINHO_GIGANTE].play()
                espinho_gigante = atual
                g = EspinhoGigante(assets, blocos)
                todos_sprites.add(g)
                todos_espinhos_gigantes.add(g)

            # Recria a plataforma após ALGUM TEMPO --> ATENÇÃO
            if atual - ultima_plataforma > 60000:
                ultima_plataforma = atual
                p = PlataformaMóvel(assets[BLOCO_IMG], blocos)
                todos_sprites.add(p)
                blocos.add(p)

            # Determina um tempo máximo de jogo
            if atual - comeco_jogo > 1000000:
                estado = FINAL #Mudar para ganhando quando colocarmos a tela de vencedor

            # Indica as colisões do jogador com cogumelos e espinhos
            dano = pygame.sprite.spritecollide(jogador, todos_espinhos, True,  pygame.sprite.collide_mask)
            ganhando_vida = pygame.sprite.spritecollide(jogador, todos_cogumelos, True,  pygame.sprite.collide_mask)
            dano_gigante = pygame.sprite.spritecollide(jogador, todos_espinhos_gigantes, True,  pygame.sprite.collide_mask)
            pisando = pygame.sprite.spritecollide(jogador, blocos, False,  pygame.sprite.collide_mask)

            # O espinho é destruido e precisa ser recriado
            for esp in dano:
                e = Espinho(assets, grupos)
                todos_sprites.add(e)
                todos_espinhos.add(e)  
    
            # Se o jogador encostou no espinho
            if len(dano) > 0:
                jogador.kill
                vidas -= 1
                estado = PERDENDO_VIDAS
                if vidas == 0:
                    estado = MORRENDO
                    assets[TRILHA_SONORA].stop()
                    assets[SOM_MORTE].play
                    game_over = GameOver(jogador.rect.center, assets)
                    todos_sprites.add(game_over)
                else:
                    assets[SOM_DANO].play
                    contato = Contato(jogador.rect.center, assets)
                    todos_sprites.add(contato)
                    piscando_tick = pygame.time.get_ticks()
                    piscando_duracao = contato.frame_ticks * len(contato.piscando_anim)
                keys_down = {}
                print(contato)

            # Se o jogador encostou no cogumelo
            if len(ganhando_vida) > 0:
                assets[SOM_COGUMELO].play()
                vidas += 1

            # Se o jogador encosta no espinho gigante
            if len(dano_gigante) > 0:
                jogador.kill()
                vidas -= 1
                estado = PERDENDO_VIDAS
                if vidas == 0:
                    estado = MORRENDO
                    assets[TRILHA_SONORA].stop
                    assets[SOM_DANO].play()
                    game_over = GameOver(jogador.rect.center, assets)
                    todos_sprites.add(game_over)
                else:
                    assets[SOM_DANO].play
                    contato = Contato(jogador.rect.center, assets)
                    todos_sprites.add(contato)
                    piscando_tick = pygame.time.get_ticks()
                    piscando_duracao = contato.frame_ticks * len(contato.piscando_anim)
                keys_down = {}
                print(contato)
                

        # Se o jogador perdeu uma vida
        elif estado == MORRENDO:
            if not game_over.alive():
                estado = FINAL
            elif estado == PERDENDO_VIDAS:
                if not contato.alive():
                    jogador = Peach(grupos, assets, linha, coluna)
                    todos_sprites.add(jogador)
                    estado = JOGANDO
            elif estado == PERDENDO_VIDAS:
                if not game_over.alive():
                    estado = FINAL
        
        # Desenha os sprites
        todos_sprites.draw(window)
        window.blit(plataforma.image, plataforma.rect)

        # Desenha as vidas
        text_surface = assets[CORACAO].render(chr(9829) * vidas, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10,10)
        window.blit(text_surface, text_rect)
        
        pygame.display.update()

    return END

game_screen(window)
