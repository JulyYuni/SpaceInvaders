'''''''''''IMPORTS'''''''''
from PPlay.window import *
from PPlay.sprite import *



'''''''''''VARIÁVEIS'''''''''

# Variáveis novo jogo
gamestate = 0                   # Inicializa no menu
iniciando_novo_jogo = True      # Um novo jogo está sendo iniciado
inicializou_gamestate = False   # O cenário não foi criado ainda

# Variáveis Numéricas
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
i = 10
j = 6
vel_horizontal_inimigo = 1
vel_vertical_inimigo = 5


# Definindo os sprites
    #Botões normais
botao_play = Sprite("assets/images/buttons/botao-play.png", 1)
botao_dificuldade = Sprite("assets/images/buttons/botao-dificuldade.png", 1)
botao_ranking = Sprite("assets/images/buttons/botao-ranking.png", 1)
botao_sair = Sprite("assets/images/buttons/botao-sair.png", 1)
button_facil = Sprite("assets/images/buttons/botao-dificuldade1.png", 1)
button_medio = Sprite("assets/images/buttons/botao-dificuldade2.png", 1)
button_dificil = Sprite("assets/images/buttons/botao-dificuldade3.png", 1)

    #Definindo os botoes em hover
botao_play_hover = Sprite("assets/images/hover-buttons/botao-play-hover.png", 1)
botao_dificuldade_hover = Sprite("assets/images/hover-buttons/botao-dificuldade-hover.png", 1)
botao_ranking_hover = Sprite("assets/images/hover-buttons/botao-ranking-hover.png", 1)
botao_sair_hover = Sprite("assets/images/hover-buttons/botao-sair-hover.png", 1)

button_facil_hover = Sprite("assets/images/hover-buttons/botao-dificuldade1-hover.png", 1)
button_medio_hover = Sprite("assets/images/hover-buttons/botao-dificuldade2-hover.png", 1)
button_dificil_hover = Sprite("assets/images/hover-buttons/botao-dificuldade3-hover.png", 1)

    #Definindo sprites de objetos
nave = Sprite('assets/images/objects/nave.png', 1)
tiro = Sprite('assets/images/objects/tiro.png', 1)
matriz_inimigos = [[Sprite('assets/images/objects/inimigo.png', 1) for _ in range(j)] for _ in range(i)]   #Inicializa a matriz de inimigos

    #Definindo backgrounds
background = Sprite("assets/images/backgrounds/plano-de-fundo.jpg", 1)
background_menu = Sprite("assets/images/backgrounds/plano-de-fundo-menu.jpg", 1)


# Obter a resolução da tela
resolution = pygame.display.Info()
resolucao_altura_tela = resolution.current_h
resolucao_largura_tela = resolution.current_w


# Criando a Janela
janela = Window(resolucao_largura_tela, resolucao_altura_tela)


# Inicialidando o recebimento de entradas
teclado = Window.get_keyboard()             #Teclado
mouse_object = Window.get_mouse()           #Mouse


# Inicializa o relógio
clock = pygame.time.Clock()
