# Importa as bibliotecas necessárias
import pygame

# Importa os arquivos do jogo
from Configuracao import *
from Assets import *
from Sprites import *


def game_screen(window, assets):
    # Ajusta a velocidade do jogo
    clock = pygame.time.Clock()

    # Cria os grupos dos sprites
    todos_sprites = pygame.sprite.Group()
    todos_espinhos = pygame.sprite.Group()
    todos_cogumelos = pygame.sprite.Group()
    todos_espinhos_gigantes = pygame.sprite.Group()
    todas_chaves = pygame.sprite.Group()
    blocos = pygame.sprite.Group()

    # Cria dicionário dos sprites
    grupos = {}
    grupos['todos_sprites'] = todos_sprites
    grupos['todos_espinhos'] = todos_espinhos
    grupos['todos_cogumelos'] = todos_cogumelos
    grupos['todos_espinhos_gigantes'] = todos_espinhos_gigantes
    grupos['todas_chaves'] = todas_chaves
    grupos['blocos'] = blocos

    # Cria fundo do jogo
    fundo_rect = assets[FUNDO].get_rect()
    
    # Cria blocos de acordo com o mapa
    for linha in range(len(MAPA)):
        for coluna in range(len(MAPA[linha])):
            tipo_bloco = MAPA[linha][coluna]
            # Verifica se deve ser inserido o bloco no jogo
            if tipo_bloco == BLOCO:
                tile = Blocos(grupos, assets, linha, coluna)
                todos_sprites.add(tile)
                blocos.add(tile)
                           
    # Cria o jogador
    jogador = Peach(grupos, assets, 14, 0)
    todos_sprites.add(jogador)
    
    # Cria os espinhos
    for i in range(2):
        espinho = Espinho(assets, grupos)
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

    
    # Cria os estados do jogador
    FINAL = 0 # Estado para a tela fechar
    JOGANDO = 1 # Estado enquanto o jogador tem vidas
    MORRENDO = 2 # Estado quando o jogador não tem mais vidas ()
    PERDENDO_VIDAS = 3 # Estado quando o jogador perde uma vida
    GANHANDO = 4 # Estado quando acabou o tempo e o jogador não perdeu

    # Cria as vidas do jogador
    vidas = 3
    keys_down = {}

    # ===================== Loop principal ==========================
    
    # Define o estado atual do jogador
    estado = JOGANDO
    
    # Define as variáveis para contagem do tempo
    ultimo_cogumelo = pygame.time.get_ticks()
    ultimo_espinho_gigante = pygame.time.get_ticks()
    ultima_plataforma = pygame.time.get_ticks()
    ultima_chave = pygame.time.get_ticks()
    comeco_jogo = pygame.time.get_ticks()

    # Carrega a imagem da trilha sonora
    assets[TRILHA_SONORA].play()

    # Estabelece as condições do jogo
    while estado != QUIT:
        clock.tick(FPS)
        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                estado = QUIT
            # Verifica se o jogador apertou alguma tecla
            if estado == JOGANDO:
                if event.type == pygame.KEYDOWN:
                    # Altera a velocidade
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        jogador.velocidadex -= VELOCIDADE_X
                    if event.key == pygame.K_RIGHT:
                        jogador.velocidadex += VELOCIDADE_X
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        jogador.jump()
                # Verifica se o jogador soltou alguma tecla
                if event.type == pygame.KEYUP:
                    # Altera a velocidade
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            jogador.velocidadex += VELOCIDADE_X
                        if event.key == pygame.K_RIGHT:
                            jogador.velocidadex -= VELOCIDADE_X

        # Atualiza a posição dos sprites
        todos_sprites.update()
        
        # Atualiza posicao da imagem de fundo
        fundo_rect.y -= VELOCIDADE_FUNDO
        
        # Verifica se o fundo saiu para baixo
        if fundo_rect.top > ALTURA:
            fundo_rect.y -= fundo_rect.height
        
        # Verifica se houve contato da Peach com o cogumelo ou espinho
        if estado == JOGANDO:
            # Define o momento atual do jogo
            atual = pygame.time.get_ticks()
            
            # Recria o cogumelo após 45 segundos que o último apareceu
            if atual - ultimo_cogumelo > 45000:
                ultimo_cogumelo = atual
                c = Cogumelo(assets, grupos)
                todos_sprites.add(c)
                todos_cogumelos.add(c)      

            # Recria o espinho gigante após 60 segundos que o último apareceu
            if atual - ultimo_espinho_gigante > 20000:
                assets[TRILHA_SONORA].stop()
                assets[SOM_ESPINHO_GIGANTE].play()
                ultimo_espinho_gigante = atual
                g = EspinhoGigante(assets, grupos)
                todos_sprites.add(g)
                todos_espinhos_gigantes.add(g)

            # Recria a plataforma após 60 segundos que a última apareceu
            if atual - ultima_plataforma > 20000:
                ultima_plataforma = atual
                p = PlataformaMóvel(assets, grupos)
                todos_sprites.add(p)
                blocos.add(p)

            # Determina um tempo máximo de jogo e, se sobreviver o jogador ganha
            if atual - ultima_chave > 10000:
                ultima_chave = atual
                ch = Chave(assets, grupos)
                todos_sprites.add(ch)
                todas_chaves.add(ch)

            # Indica as colisões do jogador com os sprites
            # Cria uma lista de danos causados pelo espinho
            dano = pygame.sprite.spritecollide(jogador, todos_espinhos, True,  pygame.sprite.collide_mask)
            # Cria uma lista dos contatos entre o jogador e os cogumelos
            ganhando_vida = pygame.sprite.spritecollide(jogador, todos_cogumelos, True,  pygame.sprite.collide_mask)
            # Cria uma lista de danos causados pelo espinho gigante
            dano_gigante = pygame.sprite.spritecollide(jogador, todos_espinhos_gigantes, True,  pygame.sprite.collide_mask)
            # Cria uma lista de contato da Peach e a chave
            salvando_mario = pygame.sprite.spritecollide(jogador, todas_chaves, True, pygame.sprite.collide_mask)

            # Para cada espinho destruído, outro é criado
            for esp in dano:
                e = Espinho(assets, grupos)
                todos_sprites.add(e)
                todos_espinhos.add(e)  
    
            # Se o jogador encostou no espinho:
            if len(dano) > 0:
                # Faz a imagem do jogador desaparecer
                jogador.kill()
                # Faz o jogador perder uma vida
                vidas -= 1
                # Muda o estado do jogador
                estado = PERDENDO_VIDAS
                # Se as vidas acabarem:
                if vidas == 0:
                    # Muda o estado do jogador
                    estado = MORRENDO
                    # Interrompe o som da trilha sonora
                    assets[TRILHA_SONORA].stop()
                    assets[SOM_ESPINHO_GIGANTE].stop()
                    # Inicia o som de morte
                    assets[SOM_MORTE].play()
                    # Carrega a animação de game over (DIMINUINDO_ANIM)
                    game_over = GameOver(jogador.rect.center, assets)
                    todos_sprites.add(game_over)
                else:
                    # Carrega a animação do contato (PISCANDO_ANIM)
                    contato = Contato(jogador.rect.center, assets)
                    todos_sprites.add(contato)
                    # Inicia o som do dano
                    assets[SOM_DANO].play()
                    # Define o tempo de animação
                    piscando_tick = pygame.time.get_ticks()
                    piscando_duracao = contato.frame_ticks * len(contato.piscando_anim)
                keys_down = {}

            # Se o jogador encostou no cogumelo:
            if len(ganhando_vida) > 0:
                # Inicia o som de ganho da vida
                assets[SOM_COGUMELO].play()
                # Jogador ganha um vida
                vidas += 1

            # Se a Peach encostar na chave:    
            if len(salvando_mario) > 0:
                # Interrompe as músicas
                assets[TRILHA_SONORA].stop()
                assets[SOM_ESPINHO_GIGANTE].stop()
                # Muda o estado do jogador
                estado = GANHANDO
                # Carrega a tela de vencedor
                return WIN

            # Se o jogador encosta no espinho gigante:
            if len(dano_gigante) > 0:
                # Faz a imagem do jogador desaparecer
                jogador.kill()
                # Verifica se o esinho gigante ainda está na tela
                if len(todos_espinhos_gigantes) == 0:
                    # Inicia o som do espinho gigante
                    assets[SOM_ESPINHO_GIGANTE].stop()
                    # Reinicia a trilha sonora
                    assets[TRILHA_SONORA].play()
                # Jogador perde uma vida
                vidas -= 1
                # Muda o estado do jogador
                estado = PERDENDO_VIDAS
                # Verifica a quantidade de vidas do jogador
                if vidas == 0:
                    # Muda o estado do jogador
                    estado = MORRENDO
                    # Interrompe o som da trilha sonora
                    assets[TRILHA_SONORA].stop()
                    # Interrompe o som do espinho gigante
                    assets[SOM_ESPINHO_GIGANTE].stop()
                    # Inicia o som do dano
                    assets[SOM_MORTE].play()
                    # Carrega a animação de game over (DIMINUINDO_ANIM)
                    game_over = GameOver(jogador.rect.center, assets)
                    todos_sprites.add(game_over)
                else:
                    # Inicia o som do dano
                    assets[SOM_DANO].play()
                    # Carrega a animação de dano (PISCANDO_ANIM)
                    contato = Contato(jogador.rect.center, assets)
                    todos_sprites.add(contato)
                    # Define o tempo de animação
                    piscando_tick = pygame.time.get_ticks()
                    piscando_duracao = contato.frame_ticks * len(contato.piscando_anim)
                keys_down = {}

            # Para cada espinho gigante que é colocado em jogo:
            for espinho_gigante in todos_espinhos_gigantes:
                # Verifica se saiu da tela
                if espinho_gigante.rect.right < 0 or espinho_gigante.rect.left > LARGURA:
                    # Faz a imagem do espinho gigante desaparecer
                    espinho_gigante.kill()
                    # Verifica se a lista dos espinhos gigantes está vazia
                    if len(todos_espinhos_gigantes) == 0:
                        # Interrompe o som do espinho gigante
                        assets[SOM_ESPINHO_GIGANTE].stop()
                        # Reinicia a trilha sonora
                        assets[TRILHA_SONORA].play()

        # Se a acabaram as vidas do jogador:
        elif estado == MORRENDO:
            # Verifica se a animação de morte já acabou
            if not game_over.alive():
                # Interrompe a trilha sonora
                assets[TRILHA_SONORA].stop()
                # Carrega a tela de game over
                return LOSE
        
        # Se o jogador perdeu uma vida:
        elif estado == PERDENDO_VIDAS:
            # Verifica se a animação do dano já acabou
            if not contato.alive():
                # Recria o jogador
                jogador = Peach(grupos, assets, linha, coluna)
                todos_sprites.add(jogador)
                # Muda o estado do jogador
                estado = JOGANDO

        # Preenche a janela com a cor branca
        window.fill((0, 0, 0))  
         
        # Redesenha o fundo em que a parte de cima deve ser continuação da parte de baixo
        window.blit(assets[FUNDO], fundo_rect)

        # Desenha o fundo com cópia pra cima
        fundo_rect2 = fundo_rect.copy()
        # Verifica se o fundo passou da tela e redesenha
        if fundo_rect.top > 0:
            fundo_rect2.y -= fundo_rect2.height
        # Preenche a janela novamente
        window.blit(assets[FUNDO], fundo_rect2)
        
        # Desenha os sprites
        todos_sprites.draw(window)
        window.blit(plataforma.image, plataforma.rect)

        # Desenha as vidas
        text_surface = assets[CORACAO].render(chr(9829) * vidas, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10,10)
        window.blit(text_surface, text_rect)
        
        # Atualiza o jogo
        pygame.display.update()