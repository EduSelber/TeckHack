# TeckHack

# Scanner de Portas com Banner Grabbing

Este é um script em Python para realizar a varredura de portas em um host ou rede, identificando quais portas estão abertas, fechadas ou filtradas. Além disso, ele faz o banner grabbing para tentar identificar o sistema operacional ou serviço em execução na porta aberta.

## Funcionalidades
- Varredura de portas em um único host (IPv4 ou IPv6) ou em uma rede inteira.
- Identificação do serviço associado às portas utilizando um dicionário de portas bem conhecidas.
- Banner grabbing para tentar identificar o sistema operacional ou serviço a partir da resposta do banner.
- Execução multithreaded para maior velocidade na varredura de portas.

## Pré-requisitos
- Python 3.x
- Bibliotecas necessárias: `socket`, `sys`, `concurrent.futures`, `tqdm`, `ipaddress`

## Instalação
1. Clone o repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/EduSelber/TeckHack.git
    ```

2. Instale as dependências necessárias utilizando `pip`:
    ```bash
    pip install tqdm
    ```

## Como Executar
1. Abra um terminal na pasta onde o script está localizado.

2. Execute o script com:
    ```bash
    python roteiro1.py
    ```

3. Escolha o tipo de varredura:
    - `single`: Para escanear um único host (IPv4, IPv6 ou hostname)
    - `network`: Para escanear uma rede inteira

### Varredura em Host Único
- Escolha a opção `single`
- Digite o endereço IP (IPv4 ou IPv6) ou hostname do alvo.
- Informe a porta inicial e a porta final para a varredura.

Exemplo:

Would you like to scan a single host or a network? (single/network): single   
Enter the IP(Ipv4 or Ipv6) address or hostname of the target server/host: 192.168.1.1   
Enter the starting port: 20   
Enter the ending port: 100  

### Varredura em Rede
- Escolha a opção `network`  
- Digite o endereço da rede(ex: `192.168.1.0`)
- Digite a subnet mask  
- Informe a porta inicial e a porta final para a varredura.  

Exemplo:  
Would you like to scan a single host or a network? (single/network): network  
Enter the network IP: 192.168.1.0  
Enter the subnet mask (between 0 and 32): 28  
Enter the starting port: 20  
Enter the ending port: 100  


## Possíveis Resultados
- **Open**: A porta está aberta e acessível.
- **Closed**: A porta está fechada no host alvo.
- **Filtered**: A porta está bloqueada por um firewall ou filtro de rede.
- **No banner available**: Não foi possível obter um banner da porta aberta.
- **Banner**: Caso o banner seja recuperado, será exibido o texto do banner e o sistema operacional ou serviço detectado.

Exemplo de saída:  
Would you like to scan a single host or a network? (single/network): single  
Enter the IP(Ipv4 or Ipv6) address or hostname of the target server/host:  scanme.nmap.org  
Resolving host scanme.nmap.org to IPv4: 45.33.32.156  
Enter the starting port: 1  
Enter the ending port: 600  
Scanning host with IP: 45.33.32.156 from port 1 to 600  
Scanning Ports: 100%|████████████████████████████████████████████| 600/600 [00:01<00:00, 530.55it/s]  

Port Scan Results:  
Port 1-21 - Status: Filtered  
Port 22 - Status: Open - Service: ssh  
Port 23-79 - Status: Filtered  
Port 80 - Status: Open - Service: http  
Port 81-600 - Status: Filtered  

Banner Grabbing  
Port 22 - Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13 - OS Detected: Linux  
Port 80 - No banner available  
Scan completed.  


## Observações
- O script utiliza até 1000 threads simultâneas para acelerar o processo de varredura.
- A detecção de sistema operacional é baseada no conteúdo do banner retornado pelo serviço na porta aberta.


