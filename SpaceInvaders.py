'''''''''''IMPORTS'''''''''
from menuPrincipal import menu_principal
from variables import gamestate, inicializou_gamestate, iniciando_novo_jogo             #Gamestate inicia com 0, gerou_cenario com False e iniciando_novo_jogo com True



'''''''''''EXECUÇÃO'''''''''

if __name__ == "__main__":
    menu_principal(gamestate, inicializou_gamestate, iniciando_novo_jogo)  