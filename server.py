# Importação de bibliotecas XML-RPC
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Importação de bibliotecas para leitura do sistema e configuração do terminal
import os
import platform

# Função para identificar o sistema e limpar o terminal
def limpar_terminal():
    sistema_operacional = platform.system()
    if sistema_operacional == 'Linux' or sistema_operacional == 'Darwin':  # Verifica se é Linux ou MacOS
        os.system('clear')
    elif sistema_operacional == 'Windows':  # Verifica se é Windows
        os.system('cls')
    else:
        print("Sistema operacional não suportado.")

# Define a classe de jogo do servidor
class Jogo:
    # Define o tamanho do tabuleiro e suas configurações 
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(9)] for _ in range(10)]  # Inicializa o tabuleiro vazio
        self.tabuleiro[0] = [str(i) for i in range(1, 10)]  # Adiciona uma linha numerada de 1 a 9
        self.tabuleiro[0][0] = '                      1'

        self.vez = 'X'  # Inicializa com a vez do jogador X
        self.ganhador = ' ' # Inicializado com ' ' pra identificar que não possui ganhador

    # Função que retorna o tabuleiro
    def print_tabuleiro(self):
        return '                      \n                      '.join(['|'.join(linha) for linha in self.tabuleiro])

    # Função que executa uma série de verificações e, após a conclusão de todas, realiza o movimento
    def movimentar(self, coluna, player):

        # Verifica se ja existe ganhador
        if self.ganhador != ' ':
            return self.ganhador

        # Verifica de quem e a vez de jogar
        if self.verificar_vez(player):
            
            for linha in range(9, -1, -1):
                # Verifica se está disponível para executar a jogada
                if self.tabuleiro[linha][coluna] == ' ':
                    self.tabuleiro[linha][coluna] = player

                    if self.vez == 'X':
                        self.vez = 'O'
                    else:
                        self.vez = 'X'
                        
                    # Verifica se apoz a jogada, o player ganhou o jogo
                    if self.verificar_ganhador(player):
                        self.ganhador = player
                        return player

                    return True
                
            # Retorna False caso a jogada não possa ser feita
            return False
        
        # Retorna False caso não seja a vez dele jogar
        else:
            return 'Vez do oponente.'

    # Função que verifica de quem é a vez, e aguarda o comando dele
    def verificar_vez(self, player):
        if player == self.vez:
            return True
        else:
            return False

    # Função que verifica se já existe um ganhador
    def verificar_ganhador(self, player):
        # Verifica as linhas
        for linha in range(1, 10):
            for x in range(0, 6):
                if self.tabuleiro[linha][x] == self.tabuleiro[linha][x+1] == self.tabuleiro[linha][x+2] == self.tabuleiro[linha][x+3] == player:
                    return True
                
        # Verifica as colunas
        for coluna in range(0, 9):
            for x in range(1, 7):
                if self.tabuleiro[x][coluna] == self.tabuleiro[x+1][coluna] == self.tabuleiro[x+2][coluna] == self.tabuleiro[x+3][coluna] == player:
                    return True

        # Verifica as diagonais
        for linha in range(1, 7):
            for coluna in range(0, 6):
                if self.tabuleiro[linha][coluna] == self.tabuleiro[linha+1][coluna+1] == self.tabuleiro[linha+2][coluna+2] == self.tabuleiro[linha+3][coluna+3] == player:
                    return True
        for linha in range(1, 7):
            for coluna in range(3, 9):
                if self.tabuleiro[linha][coluna] == self.tabuleiro[linha+1][coluna-1] == self.tabuleiro[linha+2][coluna-2] == self.tabuleiro[linha+3][coluna-3] == player:
                    return True

    def retorna_ganhador(self):
        return self.ganhador

# Restringe as chamadas para apenas um local
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Cria o servidor
with SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registra a classe do servidor
    server.register_instance(Jogo())

    limpar_terminal()
    # Inicia o servidor
    print("Servidor iniciado na porta 8000...")
    server.serve_forever()
