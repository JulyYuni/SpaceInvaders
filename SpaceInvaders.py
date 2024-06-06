
'''''''''''IMPORTS'''''''''
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.mouse import *



'''''''''''VARIÁVEIS'''''''''

# Variáveis Numéricas
gamestate = 0
aux = False
porcentagem_janela_width = 2
porcentagem_botao_width = 2
porcentagem_botao_height = 4

    #Tiros
tiros = []
tempo_transcorrido = 0
tempo_atual = 0
tempo_ultimo_tiro = 0

    #Inimigos
i = 7
j = 5
vel_horizontal_inimigo = 300
vel_vertical_inimigo = 50


# Definindo os sprites
botao_play = Sprite("Imagens/botao-play.png", 1)
botao_dificuldade = Sprite("Imagens/botao-dificuldade.png", 1)
botao_ranking = Sprite("Imagens/botao-ranking.png", 1)
botao_sair = Sprite("Imagens/botao-sair.png", 1)
button_facil = Sprite("Imagens/botao-dificuldade1.png", 1)
button_medio = Sprite("Imagens/botao-dificuldade2.png", 1)
button_dificil = Sprite("Imagens/botao-dificuldade3.png", 1)

    # Definindo os botoes em hover
botao_play_hover = Sprite("Imagens/botao-play-hover.png", 1)
botao_dificuldade_hover = Sprite("Imagens/botao-dificuldade-hover.png", 1)
botao_ranking_hover = Sprite("Imagens/botao-ranking-hover.png", 1)
botao_sair_hover = Sprite("Imagens/botao-sair-hover.png", 1)

    # Outros sprites
nave = Sprite('Imagens/nave.png', 1)
background = Sprite("Imagens/plano-de-fundo.jpg", 1)
background_menu = Sprite("Imagens/plano-de-fundo-menu.jpg", 1)
tiro = Sprite('Imagens/tiro.png')

#Inicializa a matriz de inimigos
matriz_inimigos = [[Sprite('Imagens/inimigo.png', 1) for _ in range(j)] for _ in range(i)]

# Obter a resolução da tela
resolution = pygame.display.Info()
resolucao_altura_tela = resolution.current_h
resolucao_largura_tela = resolution.current_w

# Criando a Janela
janela = Window(resolucao_largura_tela, resolucao_altura_tela)

# Inicialidando o recebimento de entrada do teclado
teclado = Window.get_keyboard()

# Inicialidando o recebimento de entrada do mouse
mouse_object = Window.get_mouse()



'''''''''''FUNÇÕES'''''''''

#1 Menu
def menu_principal():
    global gamestate
    clickou = 0
    velocidade_nave = 500
    velocidade_tiro = 500

    #Gerando background
    gerando_cenario()

    while gamestate == 0:

        #Atualiza a posição dos botões
        posicoes()

        #Atualiza a janela
        janela.update()
        
        #Verificações do hover nos botoes
        is_hover_play = mouse_object.is_over_object(botao_play)
        is_hover_dificuldade = mouse_object.is_over_object(botao_dificuldade)
        is_hover_ranking = mouse_object.is_over_object(botao_ranking)
        is_hover_sair = mouse_object.is_over_object(botao_sair)

        #Colocando botões em hover e sprites dos botões em listas
        buttons = [botao_play, botao_dificuldade, botao_ranking, botao_sair]
        buttons_hover = [botao_play_hover, botao_dificuldade_hover, botao_ranking_hover, botao_sair_hover]
        is_hover_buttons = [is_hover_play, is_hover_dificuldade, is_hover_ranking, is_hover_sair]

        #Verificacao do click no botao esquerdo do mouse
        click_left = mouse_object.is_button_pressed(1)

        #Para cada botão em tela, verificar
        for index, hover in enumerate(is_hover_buttons):
            
            #Se o mouse estiver em cima do botão
            if hover == True:
                #Desenha e posiciona botão hover
                buttons_hover[index].draw()
                posicoes()

                #Se clickou guarde essa informação
                if click_left == True:
                    clickou = index+1

                if click_left == False and clickou > 0:
                    #Botão play clickado, abre o jogo
                    if clickou == 1:
                        gamestate = 1
                        play(velocidade_nave, velocidade_tiro)
                    
                    #Botão dificuldade clickado, abre menu dificuldades
                    if clickou == 2:
                        gamestate = 2
                        velocidade_nave, velocidade_tiro = menu_dificuldade()

                        #resetando para o menu principal
                        clickou = 0
                        gerando_cenario()

                    #Botão sair clickado, fecha o jogo
                    if clickou == 4:
                        janela.close()

            #Se o mouse não estiver em cima, desenhe o botão normal
            elif hover == False: 
                buttons[index].draw()
                posicoes()
                


#2 Função que gera o cenário
def gerando_cenario():
    #Cor da Janela
    janela.set_background_color([255,174,183])

    #Backgroung play
    if gamestate == 1:
        background.draw()
    
    #Background menu
    if gamestate == 0 or gamestate == 2:
        background_menu.draw()

    janela.update()


#3 Definição das posições de início de partida
def posicoes():
    #Botões menu principal
    botao_play.set_position((janela.width/2) - (botao_play.width/2) , (janela.height - botao_play.height *4) /5)
    botao_dificuldade.set_position((janela.width/2) - (botao_dificuldade.width/2) , (botao_play.height) + (janela.height - botao_play.height *4) /5 *2)
    botao_ranking.set_position((janela.width/2) - (botao_ranking.width/2) , (botao_play.height)*2 + (janela.height - botao_play.height *4) /5* 3)
    botao_sair.set_position((janela.width/2) - (botao_sair.width/2) , (botao_play.height)*3 + (janela.height - botao_play.height *4) /5*4)

    #Botões hover principal
    botao_play_hover.set_position((janela.width/2) - (botao_play.width/2) , (janela.height - botao_play.height *4) /5)
    botao_dificuldade_hover.set_position((janela.width/2) - (botao_dificuldade.width/2) , (botao_play.height) + (janela.height - botao_play.height *4) /5 *2)
    botao_ranking_hover.set_position((janela.width/2) - (botao_ranking.width/2) , (botao_play.height)*2 + (janela.height - botao_play.height *4) /5* 3)
    botao_sair_hover.set_position((janela.width/2) - (botao_sair.width/2) , (botao_play.height)*3 + (janela.height - botao_play.height *4) /5*4)

    #Botões menu dificuldades
    button_facil.set_position((janela.width/2) - (button_facil.width/2) , 150)
    button_medio.set_position((janela.width/2) - (button_medio.width/2) , (janela.height/3) + 150)
    button_dificil.set_position((janela.width/2) - (button_dificil.width/2) , ((janela.height/3)*2) + 150)

    #Posições play
    nave.set_position(janela.width / 2 - 50, resolucao_altura_tela - nave.height)
    tiro.set_position(nave.x +42, nave.y - 10)


#4 Função que recebe as entradas do teclado
def inputs(velocidade_nave):
    global gamestate

    #Move nave para esquerda
    if(teclado.key_pressed("LEFT") == True):
        if nave.x >= 0:
            nave.x += - velocidade_nave * janela.delta_time()

    #Move nave para direita
    if(teclado.key_pressed("RIGHT") == True):
        if nave.x <= resolucao_largura_tela - nave.width:
            nave.x += velocidade_nave * janela.delta_time()

    #Voltar para o menu
    if(teclado.key_pressed("ESC")):
        gamestate = 0
        menu_principal()

#5 Tiro da bola
def input_space(tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual):
    #Solta tiro
    if(teclado.key_pressed("space") == True):
        tempo_atual = tempo_transcorrido

        if tempo_atual - tempo_ultimo_tiro > 0.5:  # Permitir um intervalo de 0.5 segundos entre os tiros
            novo_tiro = Sprite('Imagens/tiro.png')
            novo_tiro.set_position(nave.x + 42, nave.y - 10)
            tiros.append(novo_tiro)
            tempo_ultimo_tiro = tempo_atual  # Atualiza o tempo do último tiro

    return tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual

#6 Play
def play(velocidade_nave, velocidade_tiro):
    global gamestate
    desenhou_inimigos = 0
    direcao_inimigos = 1

    #Tiros
    tiros = []
    tempo_transcorrido = 0
    tempo_atual = 0
    tempo_ultimo_tiro = 0

    #Definindo posições
    posicoes()

    #Cenário é criado
    gerando_cenario()

    while gamestate == 1:

        #Desenhando sprites na tela
        background.draw()
        nave.draw()

        #Atualiza tempo passado
        tempo_transcorrido += janela.delta_time()

        #Recebe entradas do teclado
        inputs(velocidade_nave)

        #Solta tiro
        tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual = input_space(tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual)

        #Inimigos andando
        desenhou_inimigos, direcao_inimigos, gamestate = movendo_inimigos(matriz_inimigos, i, j, desenhou_inimigos, direcao_inimigos, gamestate)

        #Move e desenha os tiros
        for tiro in tiros:
            tiro.draw()
            tiro.y -= velocidade_tiro * janela.delta_time()

        #Remove os tiros que saíram da tela
        tiros = [tiro for tiro in tiros if tiro.y > 0]   

        janela.update()


#7 Menu de dificuldade (função que altera velocidade da nave e do tiro)
def menu_dificuldade():
    global gamestate

    clickou = 0
    velocidade_nave = 0
    velocidade_tiro = 0

    #Gerando background
    gerando_cenario()

    while gamestate == 2:

        #Desenhando os sprites
        button_facil.draw()
        button_medio.draw()
        button_dificil.draw()

        #Atualiza a posição dos botões
        posicoes()

        #Voltar para o menu
        if(teclado.key_pressed("ESC")):
            gamestate = 0
            return velocidade_nave, velocidade_tiro

        #Verificações do hover nos botoes
        is_hover_facil = mouse_object.is_over_object(button_facil)
        is_hover_medio = mouse_object.is_over_object(button_medio)
        is_hover_dificil = mouse_object.is_over_object(button_dificil)
        
        #Colocando botões em hover em listas
        is_hover_dificuldades = [is_hover_facil, is_hover_medio, is_hover_dificil]

        #Verificacao do click no botao esquerdo do mouse
        click = mouse_object.is_button_pressed(1)

        #Verificando para cada botão se o mouse está em cima e se foi clicado
        for index, hover in enumerate(is_hover_dificuldades):
            if hover == True:
                if click == True:
                    clickou = 1
                if clickou == 1 and click == False:
                    clickou = 0
                    if index == 0:
                        velocidade_nave = 500
                        velocidade_tiro = 500
                    if index == 1:
                        velocidade_nave = 250
                        velocidade_tiro = 250
                    if index == 2:
                        velocidade_nave = 100
                        velocidade_tiro = 100

        #Atualiza a janela
        janela.update()


#8 Movendo inimigos
def movendo_inimigos(matriz_inimigos, i, j, desenhou_inimigos, direcao_inimigos, gamestate):
    inverte_direcao = False
    gamestate= 1

    # X percorre cada linha e Y percorre cada elemento da matriz e desenha os inimigos
     #Se for a primeira vez define a posição inicial
    for x in range(i):
        for y in range(j):

            if not desenhou_inimigos:
                matriz_inimigos[x][y].set_position(573+ x * matriz_inimigos[x][y].width, 100 + y * matriz_inimigos[x][y].height)
            #Desenha inimigos
            matriz_inimigos[x][y].draw()

    #Não é mais a primeira vez desenhando"""
    desenhou_inimigos = 1

    #movimento dos inimigos   
    for i, linha in enumerate(matriz_inimigos):
        for j, inimigo in enumerate(linha):
            inimigo.x += (direcao_inimigos * vel_horizontal_inimigo * janela.delta_time())

            if (direcao_inimigos == 1 and inimigo.x + inimigo.width >= janela.width) or (direcao_inimigos == -1 and inimigo.x <= 0):
                inverte_direcao = True

            if inimigo.y + inimigo.height >= nave.y:
                gamestate = 0
                gamestate = 0


    if inverte_direcao:
        direcao_inimigos *= -1
        for linha in matriz_inimigos:
            for inimigo in linha:
                inimigo.y += (vel_vertical_inimigo)
        

    
    return desenhou_inimigos, direcao_inimigos, gamestate


# EXECUÇÃO
if __name__ == "__main__":
    menu_principal()  