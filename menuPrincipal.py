'''''''''''IMPORTS'''''''''
from functions import  *
from play import play_func
from menuDifficulty import menu_dificuldade



'''''''''''FUNÇÕES'''''''''

#1 Menu
def menu_principal(gamestate, inicializou_gamestate, iniciando_novo_jogo):
   
    while gamestate == 0:

        if not inicializou_gamestate:

            #Gera o cenário
            posicoes()
            gerando_cenario(gamestate)
            inicializou_gamestate = True        # Confirma que cenário foi gerado
            clickou = 0                         # Nenhum botão foi clickado ainda

            #Se estiver iniciando um novo jogo
            if iniciando_novo_jogo:
                #Inicializando variáveis         
                velocidade_nave = 500
                velocidade_tiro = 500

                iniciando_novo_jogo = False     # Confirma que novo jogo foi iniciado
            

        #Colocando botões em hover e sprites dos botões em listas
        buttons = [botao_play, botao_dificuldade, botao_ranking, botao_sair]
        buttons_hover = [botao_play_hover, botao_dificuldade_hover, botao_ranking_hover, botao_sair_hover]

        clickou, click_left = click_hover(clickou, buttons, buttons_hover)


        #se o botao já foi clickado, mas o usuário soltou o click
        if click_left == False and clickou > 0:
            inicializou_gamestate = False

            #Botão play clickado, abre o jogo
            if clickou == 1:
                gamestate = 1
                gamestate, inicializou_gamestate = play_func(gamestate, inicializou_gamestate, velocidade_nave, velocidade_tiro)
                continue                                                                                              
                            
            #Botão dificuldade clickado, abre menu dificuldades
            elif clickou == 2:
                gamestate = 2
                gamestate, inicializou_gamestate, velocidade_nave, velocidade_tiro = menu_dificuldade(gamestate, inicializou_gamestate)
                continue
            
            #Botão Ranking clickado, não faz nada ainda (será o gamestate = 3)
            elif clickou == 3:
                print("Ranking")

            #Botão sair clickado, fecha o jogo
            elif clickou == 4:
                janela.close()
            

        
        #Atualiza a janela
        janela.update()
