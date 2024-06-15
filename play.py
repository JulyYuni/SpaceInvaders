'''''''''''IMPORTS'''''''''
from functions import *


'''''''''''FUNÇÕES'''''''''

#1 Play
def play_func(gamestate, inicializou_gamestate, velocidade_nave, velocidade_tiro):

    while gamestate == 1:

        if not inicializou_gamestate:

            #Gera o cenário
            posicoes()
            inicializou_gamestate = True         #Confirma que cenário foi gerado

            #Tempo total do jogo
            tempo_transcorrido = 0

            #Tiros
            tiros = []
            tempo_atual = 0
            tempo_ultimo_tiro = 0

            #Inicializa a matriz de inimigos
            direcao_inimigos = 1

        #Gera o cenário
        gerando_cenario(gamestate)

        #Atualiza tempo passado
        tempo_transcorrido += janela.delta_time()
        
        #Recebe entradas do teclado
        gamestate, inicializou_gamestate = inputs(gamestate, inicializou_gamestate, velocidade_nave)
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

    return gamestate, inicializou_gamestate
        



#2 Tiro da bola
def input_space(tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual):

    #Solta tiro
    if(teclado.key_pressed("space") == True):
        tempo_atual = tempo_transcorrido

        if tempo_atual - tempo_ultimo_tiro > 0.5:  # Permitir um intervalo de 0.5 segundos entre os tiros
            novo_tiro = Sprite('assets/images/objects/tiro.png', 1)
            novo_tiro.set_position(nave.x + 42, nave.y - 10)
            tiros.append(novo_tiro)
            tempo_ultimo_tiro = tempo_atual  # Atualiza o tempo do último tiro

    return tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual




#3 Movendo inimigos
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