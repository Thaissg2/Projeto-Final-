import pygame
from Configuracao import *
from Assets import *
from Sprites import *

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
                tile = Blocos(assets[BLOCO_IMG], grupos)
                todos_sprites.add(tile)
                blocos.add(tile)
                
    # Cria o jogador
    jogador = Peach(assets[PEACH_IMG], 14, 0, grupos)
    todos_sprites.add(jogador)
    
    # Cria os espinhos
    for i in range(4):
        espinho= Espinho(assets[ESPINHO_IMG], grupos)
        todos_sprites.add(espinho)
        todos_espinhos.add(espinho)
        
    # Cria os cogumelos
    for i in range(1):
        cogumelo = Cogumelo(assets[COGUMELO_IMG], blocos)
        todos_sprites.add(cogumelo)
        todos_cogumelos.add(cogumelo)

    # Cria a plataforma
    plataforma = Plataforma(assets[PLATAFORMA_IMG])
    blocos.add(plataforma)

    # Cria os estados do jogo
    FINAL = 0
    JOGANDO = 1
    MORRENDO = 2
    estado = JOGANDO

    # Cria as vidas do jogador
    vidas = 3
    keys_down = {}

    # ===== Loop principal =====
    #tela_jogo = pygame.time.get_ticks()
    ultimo_cogumelo = pygame.time.get_ticks()
    espinho_gigante = pygame.time.get_ticks()
    ultima_plataforma = pygame.time.get_ticks()
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
                espinho_gigante = atual
                g = EspinhoGigante(assets[ESPINHO_GIGANTE_IMG], blocos)
                todos_sprites.add(g)
                todos_espinhos_gigantes.add(g)

            # Recria a plataforma após ALGUM TEMPO --> ATENÇÃO
            if atual - ultima_plataforma > 10000:
                ultima_plataforma = atual
                p = PlataformaMóvel(assets[BLOCO_IMG], blocos)
                todos_sprites.add(p)
                blocos.add(p)
        

        #if atual - tela_jogo > 10000:
            #estado = MORRENDO

        # Indica as colisões do jogador com cogumelos e espinhos
            dano = pygame.sprite.spritecollide(jogador, todos_espinhos, True,  pygame.sprite.collide_mask)
            ganhando_vida = pygame.sprite.spritecollide(jogador, todos_cogumelos, True,  pygame.sprite.collide_mask)
            dano_gigante = pygame.sprite.spritecollide(jogador, todos_espinhos_gigantes, True,  pygame.sprite.collide_mask)
            pisando = pygame.sprite.spritecollide(jogador, blocos, False,  pygame.sprite.collide_mask)

            # O espinho é destruido e precisa ser recriado
            for esp in dano:
                e = Espinho(assets[ESPINHO_IMG], blocos)
                todos_sprites.add(e)
                todos_espinhos.add(e)  
    
            # Se o jogador encostou no espinho
            if len(dano) > 0:
                assets[SOM_DANO].play()
                jogador.kill()
                vidas -= 1
                contato = Contato(jogador.rect.center, assets[PISCANDO_ANIM])
                todos_sprites.add(contato)
                estado = MORRENDO
                keys_down = {}
                piscando_tick = pygame.time.get_ticks()
                piscando_duracao = contato.frame_ticks * len(contato.piscando_anim)

            # Se o jogador encostou no cogumelo
            if len(ganhando_vida) > 0:
                assets[SOM_COGUMELO].play()
                vidas += 1

            # Se o jogador encosta no espinho gigante
            if len(dano_gigante) > 0:
                assets[SOM_DANO].play()
                jogador.kill()
                vidas -= 1
                contato = Contato(jogador.rect.center, assets[PISCANDO_ANIM])
                todos_sprites.add(contato)
                estado = MORRENDO
                keys_down = {}
                piscando_tick = pygame.time.get_ticks()
                piscando_duracao = contato.frame_ticks * len(contato.piscando_anim)
                
            #if len(pisando) > 0:
            #    self.velocidadey = 0
            
        # Se o jogador perdeu uma vida
        elif estado == MORRENDO:
            atual = pygame.time.get_ticks()
            if atual - piscando_tick > piscando_duracao:
                if vidas == 0:
                    assets[TRILHA_SONORA].stop()
                    assets[SOM_MORTE].play()
                    time.sleep(2.3)
                    estado = FINAL 
                else:
                    estado = JOGANDO
                    jogador = Peach(assets[PEACH_IMG], linha, coluna, blocos)
                    todos_sprites.add(jogador)

        # ----- Gera saídas
        window.fill((0, 0, 0))
        
        # Fazendo o fundo se mover: a parte de cima deve ser continuação da parte de baixo
        window.blit(assets[FUNDO], fundo_rect)
        # Desenha o fundo com cópia pra cima
        fundo_rect2 = fundo_rect.copy()
        if fundo_rect.top > 0:
            fundo_rect2.y -= fundo_rect2.height
        window.blit(assets[FUNDO], fundo_rect2)
        
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
