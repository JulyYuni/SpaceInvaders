'''''''''''IMPORTS'''''''''
from variables import *
from functions import *



'''''''''''FUNÇÕES'''''''''

#1 Menu de dificuldade (função que altera velocidade da nave e do tiro)
def menu_dificuldade(gamestate, inicializou_gamestate):

    while gamestate == 2:

        if not inicializou_gamestate:

            #Gera o cenário
            posicoes()
            gerando_cenario(gamestate)
            inicializou_gamestate = True         # Confirma que cenário foi gerado

            #Inicializando variáveis que a função irá retornar
            velocidade_nave = 0
            velocidade_tiro = 0

            #Nenhum botão foi clickado ainda
            clickou = 0

        
        #Colocando botões em listas
        buttons = [button_facil, button_medio, button_dificil]
        buttons_hover = [button_facil_hover, button_medio_hover, button_dificil_hover]

        clickou, click_left = click_hover(clickou, buttons, buttons_hover)

        #se o botao já foi clickado, mas o usuário soltou o click
        if click_left == False and clickou > 0:

            if clickou == 1:            # Fácil
                velocidade_nave = 500
                velocidade_tiro = 500
            elif clickou == 2:          # Médio
                velocidade_nave = 250
                velocidade_tiro = 250
            elif clickou == 3:          # Difícil
                velocidade_nave = 100
                velocidade_tiro = 100
            

        #Recebe entradas do teclado
        gamestate, inicializou_gamestate = inputs(gamestate, inicializou_gamestate, velocidade_nave)

        #Atualiza a janela
        janela.update()

    
    return gamestate, inicializou_gamestate, velocidade_nave, velocidade_tiro