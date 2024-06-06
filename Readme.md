Oi, eu sou a Júlia!

Esse projeto inclui uma versão do jogo Space Invaders que desenvolvi durante a matéria Laboratório de Jogos na faculdade.

O código foi desenvolvido em Python, utilizando as bibliotecas Pygame e PPlay.

O programa possui interface gráfica.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1 - Quanto aos sprites:
- Os sprites necessários para rodar a interface do jogo estarão sendo commitados juntamente ao código.

2 - Quanto às bibliotecas:
- Para o jogo funcionar é necessário ter o Pygame instalado.
- O PPlay é um framework para desenvolvimento de jogos na linguagem Python, com objetivo educacional. Ele foi criado no Instituto de Computação da UFF. Para mais informações, acesse: http://www2.ic.uff.br/pplay/.

3 - Quanto a instalação do PPlay no Windows ou linux (não sei como funciona em macOs):
- O PPlay não precisa de instalação, todos os arquivos necessários para a utilização do PPlay estarão sendo commitados juntamente ao código.

4 - Quanto a instalação do Pygame:
- Na barra de pequisa procure e abra um terminal (Por exemplo, no Windows, cmd(Prompt de Comando) ou Windows PowerShell. E no linux, o bash por exemplo.).
- Não é nescessário mudar o local da pasta na qual você está. A instalação será feita globalmente. 
- No terminal, escreva: pip install pygame.
- Espere a instalação ser finalizada.
- Pronto, o pygame foi instalado!
- Se quiser, você já pode fechar o terminal.

5 - Para rodar o código tudo que você precisa é:
- Baixar os arquivos do repositório corretamente.
- Mantê-los nas pastas do mesmo jeito que eles estão organizados no repositório
- Instalar o Pygame.
- Usar uma IDE que reconheça o Pygame ou rodar pelo terminal, contanto que o Pygame esteja instalado na máquina.
- O arquivo que você deve usar para rodar o jogo é o Pong.py.
- Ao executar o código será necessário digitar o nome da(o) jogadora(o).
- Obs: O repositório não possui um arquivo executável. Para abrir o jogo é necessário rodá-lo em uma IDE que reconheça a linguagem python e reconheça o pygame, da forma explicada acima.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

O que vem com nova versão

- Menu dificuldades agora ativo, mas não finalizado.
- Agora há uma partida no jogo!
- Temos uma joaninha como a nave do jogador.
- E temos borboletas como inimigos que se movem pela tela.
- A nave do jogador também pode dar tiros agora.

Tela do Jogo

- No menu principal temos o botão jogar, sair e dificuldade funcionais. O botão ranking ainda não está funcionando.
- Para mover a sua joaninha (nave) aperte os botões seta para a esquerda ou seta para a direita no teclado para movimentar para esquerda e direita, respectivamente.
- Para soltar um tiro com a nave aperte espaço.
- Para voltar ao menu aperte a tecla 'ESC' no teclado.
- Para reiniciar uma partida volte ao menu e aperte em jogar novamente.
- Para fechar o jogo aperte o botão sair no menu principal.
- Ao clickar em dificuldade no meu principal e clickar em uma das dificuldades, automaticamente a dificuldade do jogo muda. Então você agora pode apertar 'ESC', voltar para o menu e iniciar uma nova partida na dificuldade escolhida.
- Na pasta assets/images/ingame tem prints da tela do jogo rodando corretamente.

Sobre bugs e melhoras

- Atualmente os botões em dificuldade estão desalinhados e sem o hover.
- Os inimigos(Borboletas) estão andando muito rápido para facilitar os testes.
- Tiros ainda não colidem com inimigos.
- O jogo possui um bug quando se aperta espaço antes de mover a joaninha em partida, se o menu dificuldade já foi aberto. A bola trava saindo da joaninha e ela nem a bola se movem mais. Precisando apertar 'ESC' e iniciar a partida novamente para funcionar.

Considerações finais:

Esse código foi rodado no Windows e no Linux. Não sei como se comporta em MacOs.
Obrigada por visitar meu repositório. Até a proxima!