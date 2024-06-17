'''''''''''IMPORTS'''''''''
from functions import *




'''''''''''FUNÇÕES'''''''''

#1 Play
def play_func(gamestate, inicializou_gamestate, velocidade_nave, velocidade_tiro):

    while gamestate == 1:

        if not inicializou_gamestate:

            #Posicionamento dos sprites e inicialização da matriz inimigos
            posicoes()
            matriz_inimigos, direcao_inimigos = cria_posicona_matriz_inimigos() 
            
            
            #Tempo total do jogo
            tempo_transcorrido = 0

            #Tiros
            tiros = []
            tempo_atual = 0
            tempo_ultimo_tiro = 0

            #Confirma que o gamestate foi inicializado
            inicializou_gamestate = True         

        #Gera o cenário
        gerando_cenario(gamestate)
        inimigos_draw(matriz_inimigos)

        #Atualiza tempo passado
        tempo_transcorrido += janela.delta_time()
        
        #Recebe entradas do teclado
        gamestate, inicializou_gamestate = inputs(gamestate, inicializou_gamestate, velocidade_nave)

        #Solta tiro da nave
        tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual = input_space(tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual)

        #Move, desenha e remove os tiros
        tiros = move_desenha_remove_tiros(tiros, velocidade_tiro)

        #Inimigos andando
        direcao_inimigos, gamestate = movendo_inimigos(direcao_inimigos, gamestate, matriz_inimigos)

        janela.update()

    return gamestate, inicializou_gamestate
        

#2 Solta Tiro da nave
def input_space(tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual):

    #Solta tiro
    if(teclado.key_pressed("space") == True):
        
        tempo_atual = tempo_transcorrido                            # Se o space foi apertado, atualiza o tempo_atual do tiro para o tempo atual do jogo

        if tempo_atual - tempo_ultimo_tiro > 0.5:                   # Permitir um intervalo de 0.5 segundos entre os tiros
            novo_tiro = Sprite('assets/images/objects/tiro.png', 1) # Definindo novo_tiro
            novo_tiro.set_position(nave.x + 42, nave.y - 10)        # Setando posição do novo tiro no bico da nave
            tiros.append(novo_tiro)                                 # Adicionando novo tiro criado na lista de tiros em tela
            tempo_ultimo_tiro = tempo_atual                         # Atualiza o tempo do último tiro

    return tempo_transcorrido, tempo_ultimo_tiro, tiros, tempo_atual



#3 Move, desenha e remove os tiros
def move_desenha_remove_tiros(tiros, velocidade_tiro):

    #Move e desenha os tiros
        for tiro in tiros:
            tiro.draw()
            tiro.y -= velocidade_tiro * janela.delta_time()

        #Remove os tiros que saíram da tela
        tiros = [tiro for tiro in tiros if tiro.y > 0]

        return tiros

#4 Cria matriz de inimigos
def cria_posicona_matriz_inimigos():
    
    matriz_inimigos = [[None] * j for _ in range(i)]                             # Inicializa a matriz de inimigos como uma lista vazia
    direcao_inimigos = 1                                                         # Inicializa direção de inimigos horizontal para a direita
    caminhos_imagens = [caminho_inimigo_1, caminho_inimigo_2, caminho_inimigo_3] # Lista de caminhos das imagens dos inimigos

    # Preenche aleatoriamente a matriz com Sprites de 3 possíveis inimigos
    for x in range(i):
        for y in range(j):
            indice = random.randint(0, 2)                                        # Gera um índice aleatório
            caminho_imagem = caminhos_imagens[indice]                            # Pega a imagem de um inimigo aleatoriamente conforme o índice gerado
            matriz_inimigos[x][y] = Sprite(caminho_imagem, 1)                    # Para cada posição da matriz, cria um Sprite com a imagem de inimigo escolhida 

    # X percorre cada linha e Y percorre cada elemento da matriz e posiciona os inimigos na posição inicial
    for x in range(i):
        for y in range(j):
            matriz_inimigos[x][y].set_position(20 + x * (matriz_inimigos[x][y].width + matriz_inimigos[x][y].width/2), 20 + y * (matriz_inimigos[x][y].height + matriz_inimigos[x][y].width/2))
    
    return matriz_inimigos, direcao_inimigos


#5 Desenhando inimigos na tela          
def inimigos_draw(matriz_inimigos):

    # X percorre cada linha e Y percorre cada elemento da matriz e desenha os inimigos
    for x in range(i):
        for y in range(j):
            if matriz_inimigos[x][y] != None:

                #Desenha inimigos
                matriz_inimigos[x][y].draw()



#6 Movendo inimigos
def movendo_inimigos(direcao_inimigos, gamestate, matriz_inimigos):
    inverte_direcao = False                                                 # Inicializando variável que apenas essa função utiliza

    #Movimento dos inimigos   
    for linha in matriz_inimigos:
        for inimigo in linha:
            if inimigo != None:                                             # Para cada inimigo na matriz, se ele for um objeto, mova horizontalmente
                inimigo.x += (direcao_inimigos * vel_horizontal_inimigo)

                if (direcao_inimigos == 1 and inimigo.x + inimigo.width >= janela.width) or (direcao_inimigos == -1 and inimigo.x <= 0): 
                    inverte_direcao = True                                  # Se algum inimigo colidir c a parede, armazene que a direção horizontal da matriz deve ser invertida

                if inimigo.y + inimigo.height >= nave.y:
                    gamestate = 0                                           # Se algum inimigo ultrapassar a posição em y da nave, volta para o menu principal

    # Se a direção horizontal da matriz deve ser invertida
    if inverte_direcao:
        direcao_inimigos *= -1                                              # Inverta a direção da matriz
        for linha in matriz_inimigos:
            for inimigo in linha:
                if inimigo != None:                                         # Para cada inimigo na matriz, se ele for um objeto, mova verticalmente
                    inimigo.y += (vel_vertical_inimigo) 
    
    return direcao_inimigos, gamestate

