
'''''''''''IMPORTS'''''''''
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.mouse import *



'''''''''''VARIÁVEIS'''''''''

# Variáveis Numéricas
gamestate = 0
clickou = 0
aux = False
desenhou_inimigos = False
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
vel_horizontal_inimigo = 10
vel_vertical_inimigo = 50


# Definindo os sprites
botao_play = Sprite("assets/images/buttons/botao-play.png", 1)
botao_dificuldade = Sprite("assets/images/buttons/botao-dificuldade.png", 1)
botao_ranking = Sprite("assets/images/buttons/botao-ranking.png", 1)
botao_sair = Sprite("assets/images/buttons/botao-sair.png", 1)
button_facil = Sprite("assets/images/buttons/botao-dificuldade1.png", 1)
button_medio = Sprite("assets/images/buttons/botao-dificuldade2.png", 1)
button_dificil = Sprite("assets/images/buttons/botao-dificuldade3.png", 1)

    # Definindo os botoes em hover
botao_play_hover = Sprite("assets/images/hover-buttons/botao-play-hover.png", 1)
botao_dificuldade_hover = Sprite("assets/images/hover-buttons/botao-dificuldade-hover.png", 1)
botao_ranking_hover = Sprite("assets/images/hover-buttons/botao-ranking-hover.png", 1)
botao_sair_hover = Sprite("assets/images/hover-buttons/botao-sair-hover.png", 1)

button_facil_hover = Sprite("assets/images/hover-buttons/botao-dificuldade1-hover.png", 1)
button_medio_hover = Sprite("assets/images/hover-buttons/botao-dificuldade2-hover.png", 1)
button_dificil_hover = Sprite("assets/images/hover-buttons/botao-dificuldade3-hover.png", 1)

    # Definindo sprites de objetos
nave = Sprite('assets/images/objects/nave.png', 1)
tiro = Sprite('assets/images/objects/tiro.png')
matriz_inimigos = [[Sprite('assets/images/objects/inimigo.png', 1) for _ in range(j)] for _ in range(i)]   #Inicializa a matriz de inimigos

    # Definindo backgrounds
background = Sprite("assets/images/backgrounds/plano-de-fundo.jpg", 1)
background_menu = Sprite("assets/images/backgrounds/plano-de-fundo-menu.jpg", 1)

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

# Inicializa o relógio
clock = pygame.time.Clock()

'''''''''''FUNÇÕES'''''''''

#1 Menu
def menu_principal():
    global gamestate
    global clickou
    velocidade_nave = 500
    velocidade_tiro = 500
    #Atualiza a posição dos botões
    posicoes()

    #Gerando background
    gerando_cenario()

    while gamestate == 0:

        #Colocando botões em hover e sprites dos botões em listas
        buttons = [botao_play, botao_dificuldade, botao_ranking, botao_sair]
        buttons_hover = [botao_play_hover, botao_dificuldade_hover, botao_ranking_hover, botao_sair_hover]

        clickou, click_left = click_hover(buttons, buttons_hover)
        #se o botao já foi clickado, mas o usuário soltou o click
        if click_left == False and clickou > 0:
            #Botão play clickado, abre o jogo
            if clickou == 1:
                gamestate = 1
                play(velocidade_nave, velocidade_tiro)

                #Resetando para o menu principal
                clickou = 0
                posicoes()
                gerando_cenario()

                            
            #Botão dificuldade clickado, abre menu dificuldades
            elif clickou == 2:
                gamestate = 2
                velocidade_nave, velocidade_tiro = menu_dificuldade()

                #Resetando para o menu principal
                clickou = 0
                posicoes()
                gerando_cenario()

            #Botão sair clickado, fecha o jogo
            elif clickou == 4:
                janela.close()
            

        
        #Atualiza a janela
        janela.update()

#2 Desenhando inimigos na tela          
def inimigos_draw():
    # X percorre cada linha e Y percorre cada elemento da matriz e desenha os inimigos
    for x in range(i):
        for y in range(j):
            if matriz_inimigos[x][y] != None:
                #Desenha inimigos
                matriz_inimigos[x][y].draw()

#2 Função que gera o cenário
def gerando_cenario():
    #Cor da Janela
    janela.set_background_color([255,174,183])

    #Menu principal
    if gamestate == 0:
        background_menu.draw()
        botao_play.draw()
        botao_dificuldade.draw()
        botao_ranking.draw()
        botao_sair.draw()

    #Play
    if gamestate == 1:
        background.draw()
        nave.draw()
        inimigos_draw()
    
    
    #Menu dificuldades
    if gamestate == 2:
        background_menu.draw()
        button_facil.draw()
        button_medio.draw()
        button_dificil.draw()



#3 Definição das posições de início de partida
def posicoes():
    global desenhou_inimigos

    botoes_x = janela.width/2 - (botao_play.width/2)
    num_magico = (janela.height - botao_play.height *4) /5
    botao_play_y = (num_magico)
    botao_dificuldade_y = (botao_play.height) + (num_magico)*2
    botao_ranking_y = (botao_play.height)*2 + (num_magico)  *3
    botao_sair_y = (botao_play.height)*3 + (num_magico)     *4
    botao_medio_y = (button_dificil.y - button_facil.y) /2

    #Botões menu principal
    botao_play.set_position(botoes_x , botao_play_y)
    botao_dificuldade.set_position(botoes_x , botao_dificuldade_y)
    botao_ranking.set_position(botoes_x , botao_ranking_y)
    botao_sair.set_position(botoes_x , botao_sair_y)

    #Botões hover principal
    botao_play_hover.set_position(botoes_x , botao_play_y)
    botao_dificuldade_hover.set_position(botoes_x , botao_dificuldade_y)
    botao_ranking_hover.set_position(botoes_x , botao_ranking_y)
    botao_sair_hover.set_position(botoes_x , botao_sair_y)

    #Botões menu dificuldades
    button_facil.set_position(botoes_x , botao_play_y)
    button_medio.set_position(botoes_x  , botao_medio_y)
    button_dificil.set_position(botoes_x , botao_sair_y)

    #Botões menu dificuldades
    button_facil_hover.set_position(botoes_x , botao_play_y)
    button_medio_hover.set_position(botoes_x  , botao_medio_y)
    button_dificil_hover.set_position(botoes_x , botao_sair_y)

    #Posições play
    nave.set_position(janela.width / 2 - 50, resolucao_altura_tela - nave.height)
    tiro.set_position(nave.x +42, nave.y - 10)

    #Setando a posição inicial caso seja a primeira vez
    if not desenhou_inimigos:
        # X percorre cada linha e Y percorre cada elemento da matriz e desenha os inimigos
        for x in range(i):
            for y in range(j):
                matriz_inimigos[x][y].set_position(20 + x * (matriz_inimigos[x][y].width + matriz_inimigos[x][y].width/2), 20 + y * (matriz_inimigos[x][y].height + matriz_inimigos[x][y].width/2))
    
    desenhou_inimigos = True


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
        return gamestate
    
    gamestate = 1
    return gamestate
    


#5 Tiro da bola
def input_space(tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual):
    #Solta tiro
    if(teclado.key_pressed("space") == True):
        tempo_atual = tempo_transcorrido

        if tempo_atual - tempo_ultimo_tiro > 0.5:  # Permitir um intervalo de 0.5 segundos entre os tiros
            novo_tiro = Sprite('assets/images/objects/tiro.png')
            novo_tiro.set_position(nave.x + 42, nave.y - 10)
            tiros.append(novo_tiro)
            tempo_ultimo_tiro = tempo_atual  # Atualiza o tempo do último tiro

    return tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual



#6 Click e hover nos botoes
def click_hover(buttons, buttons_hover):
    global clickou

    is_hover = []

    #posicoes()
    #Verificações do hover nos botoes
    for button in buttons:
        is_hover.append(mouse_object.is_over_object(button))

    #Verificacao do click no botao esquerdo do mouse
    click_left = mouse_object.is_button_pressed(1)

    #Para cada botão em tela, verificar
    for index, hover in enumerate(is_hover): 
        #Se o mouse estiver em cima do botão
        if hover == True:
            #Desenha e posiciona botão hover
            posicoes()
            buttons_hover[index].draw()        

            #Se clickou guarde essa informação
            if click_left == True:
                clickou = index+1         

        #Se o mouse não estiver em cima, desenhe o botão normal
        elif hover == False:
            posicoes()
            buttons[index].draw()

    
    return clickou, click_left

                


#6 Play
def play(velocidade_nave, velocidade_tiro):
    global gamestate
    direcao_inimigos = 1

    #Tiros
    tiros = []
    tempo_transcorrido = 0
    tempo_atual = 0
    tempo_ultimo_tiro = 0

    # Inicializa a matriz de inimigos
    global matriz_inimigos
    global desenhou_inimigos
    matriz_inimigos = [[Sprite('assets/images/objects/inimigo.png', 1) for _ in range(j)] for _ in range(i)]      # Inicializa a matriz de inimigos
    desenhou_inimigos = False
    
    #Define posições
    posicoes()

    while gamestate == 1:

        #Cenário é criado
        gerando_cenario()

        #Atualiza tempo passado
        tempo_transcorrido += janela.delta_time()
        
        #Recebe entradas do teclado
        gamestate = inputs(velocidade_nave)
        if gamestate == 0:
            return gamestate
        #print(gamestate)
        #Solta tiro
        tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual = input_space(tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual)
        
        #Inimigos andando
        direcao_inimigos, gamestate = movendo_inimigos(direcao_inimigos, gamestate)
        
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

    velocidade_nave = 0
    velocidade_tiro = 0

    #Atualiza a posição dos botões
    posicoes()
    
    #Gerando background
    gerando_cenario()

    while gamestate == 2:
        
        #Colocando botões em hover em listas
        buttons = [button_facil, button_medio, button_dificil]
        buttons_hover = [button_facil_hover, button_medio_hover, button_dificil_hover]

        clickou, click_left = click_hover(buttons, buttons_hover)
        #se o botao já foi clickado, mas o usuário soltou o click
        if click_left == False and clickou > 0:

            if clickou == 1:
                velocidade_nave = 500
                velocidade_tiro = 500
            elif clickou == 2:
                velocidade_nave = 250
                velocidade_tiro = 250
            elif clickou == 3:
                velocidade_nave = 100
                velocidade_tiro = 100
            

        #Voltar para o menu
        if(teclado.key_pressed("ESC")):
            gamestate = 0
            return velocidade_nave, velocidade_tiro

        #Atualiza a janela
        janela.update()

#8 Movendo inimigos
def movendo_inimigos(direcao_inimigos, gamestate):
    inverte_direcao = False

    #movimento dos inimigos   
    for linha in matriz_inimigos:
        for inimigo in linha:
            if inimigo != None:
                inimigo.x += (direcao_inimigos * vel_horizontal_inimigo)

                if (direcao_inimigos == 1 and inimigo.x + inimigo.width >= janela.width) or (direcao_inimigos == -1 and inimigo.x <= 0):
                    inverte_direcao = True

                if inimigo.y + inimigo.height >= nave.y:
                    gamestate = 0


    if inverte_direcao:
        direcao_inimigos *= -1
        for linha in matriz_inimigos:
            for inimigo in linha:
                if inimigo != None:
                    inimigo.y += (vel_vertical_inimigo)
    
    return direcao_inimigos, gamestate


# EXECUÇÃO
if __name__ == "__main__":
    menu_principal()  