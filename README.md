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
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências necessárias utilizando `pip`:
    ```bash
    pip install tqdm
    ```

## Como Executar
1. Abra um terminal na pasta onde o script está localizado.

2. Execute o script com:
    ```bash
    python3 nome_do_script.py
    ```

3. Escolha o tipo de varredura:
    - `single`: Para escanear um único host (IPv4, IPv6 ou hostname)
    - `network`: Para escanear uma rede inteira

### Varredura em Host Único
- Escolha a opção `single`
- Digite o endereço IP (IPv4 ou IPv6) ou hostname do alvo.
- Informe a porta inicial e a porta final para a varredura.

Exemplo:

Would you like to scan a single host or a network? (single/network): single Enter the IP(Ipv4 or Ipv6) address or hostname of the target server/host: 192.168.1.1 Enter the starting port: 20 Enter the ending port: 100


## Possíveis Resultados
- **Open**: A porta está aberta e acessível.
- **Closed**: A porta está fechada no host alvo.
- **Filtered**: A porta está bloqueada por um firewall ou filtro de rede.
- **No banner available**: Não foi possível obter um banner da porta aberta.
- **Banner**: Caso o banner seja recuperado, será exibido o texto do banner e o sistema operacional ou serviço detectado.

Exemplo de saída:
Port Scan Results: Port 22 - Status: Open - Service: SSH Port 23 - Status: Closed Port 80 - Status: Open - Service: HTTP Port 8080 - Status: Filtered

Caso um banner seja recuperado:
Port 22 - Banner: SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2 - OS Detected: Linux Port 80 - Banner: Apache/2.4.38 (Debian) - OS Detected: Apache

## Observações
- Para a varredura de redes, o script utiliza `strict=False` para considerar IPs válidos, mesmo que não sejam o endereço de rede base.
- O script utiliza até 1000 threads simultâneas para acelerar o processo de varredura.
- A detecção de sistema operacional é baseada no conteúdo do banner retornado pelo serviço na porta aberta.


