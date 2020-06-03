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

    # Cria os estados do personagem
    FINAL = 0 #Estado para a tela fechar
    JOGANDO = 1 #Estado enquanto a personagem tem vidas
    MORRENDO = 2 #Estado quando a personagem não tem mais vidas ()
    PERDENDO_VIDAS = 3 #Estado quando a personagem perde uma vida
    #GANHANDO = 4 #Estado quando acabou o tempo e o jogador não perdeu

    # Cria as vidas do jogador
    vidas = 3
    keys_down = {}
    estado = JOGANDO
    # ===== Loop principal =====
    ultimo_cogumelo = pygame.time.get_ticks()
    ultimo_espinho_gigante = pygame.time.get_ticks()
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
            if atual - ultimo_espinho_gigante > 60000:
                assets[SOM_ESPINHO_GIGANTE].play()
                ultimo_espinho_gigante = atual
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
                if len(todos_espinhos_gigantes) == 0:
                    assets[SOM_ESPINHO_GIGANTE].stop()
                    assets[TRILHA_SONORA].play()
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
                
            for espinho_gigante in todos_espinhos_gigantes:
                # Verifica se saiu da tela
                if espinho_gigante.rect.right < 0 or espinho_gigante.rect.left > LARGURA:
                    espinho_gigante.kill()
                    if len(todos_espinhos_gigantes) == 0:
                        som_espinho_gigante.stop()
                        trilha_sonora.play()
                

        # Se o jogador perdeu uma vida
        elif estado == MORRENDO:
            if not game_over.alive():
                #estado = FINAL
                return LOSE
        elif estado == PERDENDO_VIDAS:
            if not contato.alive():
                jogador = Peach(grupos, assets, linha, coluna)
                todos_sprites.add(jogador)
                estado = JOGANDO

        # Desenha os sprites
        window.fill((0, 0, 0))  # Preenche com a cor branca
         
        # Além disso, deve ser cíclica, ou seja, a parte de cima deve ser continuação da parte de baixo
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