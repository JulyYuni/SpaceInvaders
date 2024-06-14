'''''''''''IMPORTS'''''''''
from variables import *



'''''''''''FUNÇÕES'''''''''

#1 Função que gera o cenário
def gerando_cenario(gamestate):

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



#2 Desenhando inimigos na tela          
def inimigos_draw():

    # X percorre cada linha e Y percorre cada elemento da matriz e desenha os inimigos
    for x in range(i):
        for y in range(j):
            if matriz_inimigos[x][y] != None:

                #Desenha inimigos
                matriz_inimigos[x][y].draw()



#3 Definição das posições de início de partida
def posicoes():
    global desenhou_inimigos

    botoes_x = janela.width/2 - (botao_play.width/2)
    botoes_y_gap = (janela.height - botao_play.height *4) /5
    botao_play_y = (botoes_y_gap)
    botao_dificuldade_y = (botao_play.height) + (botoes_y_gap)*2
    botao_ranking_y = (botao_play.height)*2 + (botoes_y_gap)  *3
    botao_sair_y = (botao_play.height)*3 + (botoes_y_gap)     *4
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

    #Botões hover menu dificuldades
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
def inputs(gamestate, inicializou_gamestate, velocidade_nave):  #tirar esse velocidade_nave do parametro

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
        inicializou_gamestate = False

    return gamestate, inicializou_gamestate

#6 Click e hover nos botoes
def click_hover(clickou, buttons, buttons_hover):

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