Alteracoes a serem feitas para o funcionamento do jogo em diferentes dispositivos:

Para identificar o endereço IP do seu computador em diferentes sistemas operacionais, você pode seguir as etapas abaixo:

No Windows:
    Abra o Prompt de Comando. Você pode fazer isso pressionando a tecla Win + R, digitando cmd e pressionando Enter.

    No Prompt de Comando, digite o seguinte comando e pressione Enter:
        ipconfig

    Procure a seção que corresponde à sua conexão de rede (geralmente "Adaptador de Ethernet" para conexões com fio e "Adaptador de Rede Sem Fio" para conexões sem fio). O endereço IP será listado ao lado de "Endereço IPv4".

No Ubuntu (ou outras distribuições Linux):
    Abra o Terminal. Você pode fazer isso pressionando Ctrl + Alt + T.

    No Terminal, digite o seguinte comando e pressione Enter:
        ip addr show

    Procure a seção que corresponde à sua conexão de rede (geralmente "eth0" para conexões com fio e "wlan0" para conexões sem fio). O endereço IP será listado ao lado de "inet".

Depois de pegar os ip do dispositivo que ira rodar o servidor.

Arquivo client.py:
    Identifique o endereço IP do servidor: O endereço IP do servidor ao qual você deseja se conectar deve ser conhecido. Este é o endereço IP do PC que está executando o servidor do jogo.

    Atualize o endereço IP no arquivo client.py: No arquivo client.py, localize a linha onde o ServerProxy é instanciado. Deve parecer algo assim:
        server = ServerProxy('http://172.31.117.17:8000')

    Substitua 'http://172.31.117.17:8000' pelo endereço IP do servidor ao qual você deseja se conectar. Por exemplo, se o endereço IP do servidor for 192.168.1.10, a linha deve ser alterada para:
        server = ServerProxy('http://192.168.1.10:8000')

    Execute o arquivo client.py em ambos os PCs: Agora você deve ser capaz de executar o arquivo client.py em ambos os PCs. Certifique-se de que o servidor do jogo está em execução no PC que está atuando como servidor.

    Jogue o jogo: Agora você deve ser capaz de jogar o jogo entre os dois PCs. Lembre-se de que cada jogador deve esperar a jogada do outro antes de fazer a sua.

Arquivo server.py:
    Identifique o endereço IP do servidor: O endereço IP do servidor ao qual você deseja se conectar deve ser conhecido. Este é o endereço IP do PC que está executando o servidor do jogo.

    Atualize o endereço IP no arquivo server.py: No arquivo server.py, localize a linha onde o SimpleXMLRPCServer é instanciado. Deve parecer algo assim:
        with SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler) as server:

    Substitua 'localhost' pelo endereço IP do servidor ao qual você deseja se conectar. Por exemplo, se o endereço IP do servidor for 192.168.1.10, a linha deve ser alterada para:
        with SimpleXMLRPCServer(("192.168.1.10", 8000), requestHandler=RequestHandler) as server:

    Execute o arquivo server.py no PC do servidor: Agora você deve ser capaz de executar o arquivo server.py no PC que está atuando como servidor. Certifique-se de que o firewall do PC do servidor permite conexões na porta 8000.

    Execute o arquivo client.py no PC do cliente: No PC do cliente, execute o arquivo client.py com o endereço IP do servidor atualizado, conforme descrito no tutorial anterior.

    Jogue o jogo: Agora você deve ser capaz de jogar o jogo entre os dois PCs. Lembre-se de que cada jogador deve esperar a jogada do outro antes de fazer a sua.