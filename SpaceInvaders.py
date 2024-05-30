
'''''''''''IMPORTS'''''''''
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.mouse import *



'''''''''''VARIÁVEIS'''''''''

# Variáveis Numéricas
cont = 0
aux = False

# Definindo os sprites
botao_play = Sprite("Imagens/botao-play.png", 1)
botao_dificuldade = Sprite("Imagens/botao-dificuldade.png", 1)
botao_ranking = Sprite("Imagens/botao-ranking.png", 1)
botao_sair = Sprite("Imagens/botao-sair.png", 1)
botao_dificuldade1 = Sprite("Imagens/botao-dificuldade1.png", 1)
botao_dificuldade2 = Sprite("Imagens/botao-dificuldade2.png", 1)
botao_dificuldade3 = Sprite("Imagens/botao-dificuldade3.png", 1)

# Obter a resolução da tela
resolution = pygame.display.Info()

# Criando a Janela
janela = Window(resolution.current_w, resolution.current_h)

# Inicialidando o recebimento de entrada do teclado
teclado = Window.get_keyboard()

# Inicialidando o recebimento de entrada do mouse
mouse_object = Window.get_mouse()



'''''''''''FUNÇÕES'''''''''

#1 Menu
def menu_principal():
    global cont

    while cont == 0:

        #Cor da Janela
        janela.set_background_color([255,174,183])

        #Desenhando os sprites
        botao_play.draw()
        botao_dificuldade.draw()
        botao_ranking.draw()
        botao_sair.draw()

        #Atualiza a posição dos botões
        posicoes()

        #Atualiza a janela
        janela.update()

        #Verificações do hover nos botoes
        hover_button_play = mouse_object.is_over_object(botao_play)
        hover_button_dificuldade = mouse_object.is_over_object(botao_dificuldade)
        hover_button_ranking = mouse_object.is_over_object(botao_ranking)
        hover_button_sair = mouse_object.is_over_object(botao_sair)
        hover_button_dificuldade1 = mouse_object.is_over_object(botao_dificuldade1)
        hover_button_dificuldade2 = mouse_object.is_over_object(botao_dificuldade2)
        hover_button_dificuldade3 = mouse_object.is_over_object(botao_dificuldade3)

        #Verificacao do click no botao esquerdo do mouse
        click_left = mouse_object.is_button_pressed(1)

        #Botão play clickado, abre o jogo
        if hover_button_play == True:
            if click_left == True:
                cont = 1
                play()

        #Botão dificuldade clickado, abre o novo menu, agora com dificuldades
        if hover_button_dificuldade == True:
            if click_left == True:
                cont = 2
                menu_dificuldade()

        #Botão sair clickado, fecha o jogo
        if hover_button_sair == True:
            if click_left == True:
                janela.close()


#2 Função que gera o cenário
def gerando_cenario_play():
    #Cor da Janela
    janela.set_background_color([255,174,183])
    janela.update()


#3 Definição das posições de início de partida
def posicoes():

    #Botões menu principal
    botao_play.set_position((janela.width/2) - (botao_play.width/2) , (janela.height - botao_play.height *4) /5)
    botao_dificuldade.set_position((janela.width/2) - (botao_dificuldade.width/2) , (botao_play.height) + (janela.height - botao_play.height *4) /5 *2)
    botao_ranking.set_position((janela.width/2) - (botao_ranking.width/2) , (botao_play.height)*2 + (janela.height - botao_play.height *4) /5* 3)
    botao_sair.set_position((janela.width/2) - (botao_sair.width/2) , (botao_play.height)*3 + (janela.height - botao_play.height *4) /5*4)


    #Botões menu dificuldades
    botao_dificuldade1.set_position((janela.width/2) - (botao_dificuldade1.width/2) , 75)
    botao_dificuldade2.set_position((janela.width/2) - (botao_dificuldade2.width/2) , (janela.height/3) + 75)
    botao_dificuldade3.set_position((janela.width/2) - (botao_dificuldade3.width/2) , ((janela.height/3)*2) + 75)


#4 Função que recebe as entradas do teclado
def inputs():
    global cont
    # Voltar para o menu
    if(teclado.key_pressed("ESC")):
        cont = 0


#5 Play
def play():
    global cont
    while cont == 1:
        #Cenário é criado
        gerando_cenario_play()

        #Recebe apenas o ESC no momento, que volta para o menu principal
        inputs()


#6 Menu de dificuldade
def menu_dificuldade():
    global cont
    while cont == 2:
        #Cor da Janela
        janela.set_background_color([255,174,183])
        botao_dificuldade1.draw()
        botao_dificuldade2.draw()
        botao_dificuldade3.draw()
        posicoes()
        janela.update()
        inputs()





# EXECUÇÃO
if __name__ == "__main__":
    menu_principal()  