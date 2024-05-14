# Importação de bibliotecas XML-RPC
from xmlrpc.client import ServerProxy

# Importação de bibliotecas para leitura do sistema e configuração do terminal
import os
import platform
import time

# Conecta-se ao servidor
server = ServerProxy('http://localhost:8000')

# Função para identificar o sistema e limpar o terminal
def limpar_terminal():
    sistema_operacional = platform.system()
    if sistema_operacional == 'Linux' or sistema_operacional == 'Darwin':  # Verifica se é Linux ou MacOS
        os.system('clear')
    elif sistema_operacional == 'Windows':  # Verifica se é Windows
        os.system('cls')
    else:
        print("Sistema operacional não suportado.")

# FUNÇÕES DE TEXTO/INTERFACE PARA O TERMINAL
def abertura():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=") #61 espacos
    print("               Bem-vindo ao Quatro em Linha!\n")
    print("•   O Quatro em Linha é um jogo para dois jogadores onde o \nobjetivo é ser o primeiro a formar uma linha contínua de \nquatro peças da sua cor (horizontal, vertical ou diagonal) \nno tabuleiro.")
    print("\n•   Cada jogador tem sua própria peça, representada por 'X' \ne 'O'.")
    print("\n•   Os jogadores alternam suas jogadas, escolhendo uma coluna \npara soltar uma peça na parte superior do tabuleiro. A peça \ncai até atingir a posição mais baixa disponível na coluna.")
    print("\n•   O jogo termina quando um jogador forma uma linha de \nquatro peças ou quando o tabuleiro fica completamente cheio, \nresultando em empate.")
    print("\n                  Boa sorte e divirta-se!\n")

    # Aguarda o usuário pressionar qualquer tecla para continuar
    input("Pressione qualquer tecla para continuar...")
    limpar_terminal()

def tabuleiro():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n") #61 espacos
    print_tabuleiro()

def fim_jogo(frase):
    limpar_terminal()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print("                         FIM DE JOGO!")
    print("                         Ganhador: ", frase)
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    print_tabuleiro()
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    exit()

def aguarde():
    limpar_terminal()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n") #61 espacos
    print_tabuleiro()
    print("\n•   Aguarde a jogada do inimigo antes de jogar!\n")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n") #61 espacos

# Função que recebe as linhas do tabuleiro 
def print_tabuleiro():
    print(server.print_tabuleiro())

# Função que faz o pedido do movimento e recebe o resultado da operação
def movimentar(coluna, player):
    frase = server.movimentar(coluna, player)
    
    if frase == True:
        print(' ')
    elif frase == 'Vez do oponente.':
        limpar_terminal()
        print("\n•   Não é o seu turno! Aguarde e tente novamente.")
        time.sleep(2)
        limpar_terminal()
    elif frase == 'X' or frase == 'O':
        fim_jogo(frase)
    else:
        limpar_terminal()
        print("\n•   Coluna cheia! Aguarde e tente outra coluna.")
        time.sleep(2)
        limpar_terminal()

# Loop do jogo
if __name__ == "__main__":
    limpar_terminal()

    abertura()

     # Aguarda que o jogador escolha uma opção válida de símbolo para continuar
    while True:
        player = input("\n•   Escolha seu símbolo (X ou O): ")

        if player == 'x':
            player = 'X'

        if player == 'o':
            player = 'O'

        if player == 'X' or player == 'O':
            break
        else:
            limpar_terminal()
            print('\n•   Opcao invalida! Aguarde e tente novamente.')
            time.sleep(2)
            limpar_terminal()
    
    limpar_terminal()

    while True:

        # Aguarda que o jogador escolha uma opção válida de coluna para continuar
        while True:

            # Verifica se e a vez do player, caso não seja entrara no loop de agurade
            aguarde()
            while True:
                if server.verificar_vez(player):
                    frase = server.retorna_ganhador()
                    if frase != ' ':
                        fim_jogo(frase)
                    break

            limpar_terminal()
            tabuleiro()

            try:
                coluna = int(input("\n•   Digite o número da coluna (1-9): ")) - 1

                if coluna >= 0 and coluna <= 8:
                    break
                else:
                    limpar_terminal()
                    print('\n•   Opcao invalida! Aguarde e tente novamente.')
                    time.sleep(2)
                    limpar_terminal()

            except ValueError:
                limpar_terminal()
                print('\n•   Opcao invalida! Aguarde e tente novamente.')
                time.sleep(2)
                limpar_terminal()

        limpar_terminal()
        movimentar(coluna, player)
