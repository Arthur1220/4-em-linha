<div>
    
<h1 align="center">Bem-vindo ao jogo 4 em Linha.</h1>

<p align="center">O 4 em Linha é um jogo para dois jogadores onde o objetivo é conectar quatro peças da mesma cor em linha, seja horizontal, vertical ou diagonal, em um tabuleiro. Os jogadores alternam colocando uma peça em uma coluna do tabuleiro 9x9 até que um deles consiga formar a linha de quatro peças da sua cor primeiro.</p>

##

<h2>Alteracoes a serem feitas para o funcionamento do jogo em diferentes dispositivos:</h2>

<p>Para identificar o endereço IP do seu computador em diferentes sistemas operacionais, você pode seguir as etapas abaixo:</p>

<h3>No Windows:</h3>

<p>Abra o Prompt de Comando. Você pode fazer isso pressionando a tecla Win + R, digitando cmd e pressionando Enter.</p>

<p>No Prompt de Comando, digite o seguinte comando e pressione Enter:</p>

```bash
ipconfig
```

<p>Procure a seção que corresponde à sua conexão de rede (geralmente "Adaptador de Ethernet" para conexões com fio e "Adaptador de Rede Sem Fio" para conexões sem fio). O endereço IP será listado ao lado de "Endereço IPv4".</p>

<h3>No Ubuntu (ou outras distribuições Linux):</h3>

<p>Abra o Terminal. Você pode fazer isso pressionando Ctrl + Alt + T.</p>

<p>No Terminal, digite o seguinte comando e pressione Enter:</p>

``` bash
ip addr show
```

<p>Procure a seção que corresponde à sua conexão de rede (geralmente "eth0" para conexões com fio e "wlan0" para conexões sem fio). O endereço IP será listado ao lado de "inet".</p>

##

<h2>Depois de pegar os ip do dispositivo que ira rodar o servidor.</h2>

<h3>Arquivo client.py:</h3>

<p>Identifique o endereço IP do servidor: O endereço IP do servidor ao qual você deseja se conectar deve ser conhecido. Este é o endereço IP do PC que está executando o servidor do jogo.</p>

<p>Atualize o endereço IP no arquivo client.py: No arquivo client.py, localize a linha onde o ServerProxy é instanciado. Deve parecer algo assim:</p>

``` python
server = ServerProxy('http://172.31.117.17:8000')
```

<p>Substitua 'http://172.31.117.17:8000' pelo endereço IP do servidor ao qual você deseja se conectar. Por exemplo, se o endereço IP do servidor for 192.168.1.10, a linha deve ser alterada para:</p>

``` python
server = ServerProxy('http://192.168.1.10:8000')
``` 

<p>Execute o arquivo client.py em ambos os PCs: Agora você deve ser capaz de executar o arquivo client.py em ambos os PCs. Certifique-se de que o servidor do jogo está em execução no PC que está atuando como servidor.</p>

<p>Jogue o jogo: Agora você deve ser capaz de jogar o jogo entre os dois PCs. Lembre-se de que cada jogador deve esperar a jogada do outro antes de fazer a sua.</p>

<h3>Arquivo server.py:</h3>

<p>Identifique o endereço IP do servidor: O endereço IP do servidor ao qual você deseja se conectar deve ser conhecido. Este é o endereço IP do PC que está executando o servidor do jogo.</p>

<p>Atualize o endereço IP no arquivo server.py: No arquivo server.py, localize a linha onde o SimpleXMLRPCServer é instanciado. Deve parecer algo assim:</p>

``` python
with SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler) as server:
``` 

<p>Substitua 'localhost' pelo endereço IP do servidor ao qual você deseja se conectar. Por exemplo, se o endereço IP do servidor for 192.168.1.10, a linha deve ser alterada para:</p>

``` python
with SimpleXMLRPCServer(("192.168.1.10", 8000), requestHandler=RequestHandler) as server:
``` 

<p>Execute o arquivo server.py no PC do servidor: Agora você deve ser capaz de executar o arquivo server.py no PC que está atuando como servidor. Certifique-se de que o firewall do PC do servidor permite conexões na porta 8000.</p>

<p>Execute o arquivo client.py no PC do cliente: No PC do cliente, execute o arquivo client.py com o endereço IP do servidor atualizado, conforme descrito no tutorial anterior.</p>

<p>Jogue o jogo: Agora você deve ser capaz de jogar o jogo entre os dois PCs. Lembre-se de que cada jogador deve esperar a jogada do outro antes de fazer a sua.</p>

</div>
