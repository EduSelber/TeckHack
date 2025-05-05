# TeckHack

## Ferramenta de Reconhecimento e Análise de Alvos

**TeckHack** é um conjunto de ferramentas em Python para realizar tarefas de reconhecimento em alvos online, reunindo diversas funcionalidades úteis para pentesters e analistas de segurança, como varredura de portas, consultas DNS, WHOIS, detecção de WAF e enumeração de subdomínios.

## 🔧 Funcionalidades

### 1. Scanner de Portas com Banner Grabbing (`roteiro1.py`)
- Varredura de portas (host único ou rede)
- Identificação de serviços bem conhecidos
- Coleta de banner das portas abertas
- Execução multithreaded

### 2. DNS Lookup (`dns_lookup.py`)
- Resolve um domínio para IP usando DNS padrão

### 3. WHOIS Lookup (`whois_lookup.py`)
- Consulta informações WHOIS do domínio

### 4. WAF Detection (`option4.py`)
- Detecta a presença de um WAF (Web Application Firewall) com `wafw00f`

### 5. DNS Enumeration (`dns_enumeration.py`)
- Enumera subdomínios a partir de wordlists fornecidas

## 📦 Pré-requisitos
- Python 3.x

### Instale as bibliotecas necessárias com:
```bash
pip install -r requirements.txt
```

### Exemplo de requirements.txt:
```text
tqdm
wafw00f
python-whois
```

## 💾 Instalação
1. Clone o repositório:
```bash
git clone https://github.com/EduSelber/TeckHack.git
cd TeckHack
```

2. Instale os requisitos:
```bash
pip install -r requirements.txt
```

## ▶️ Como Executar
Execute o script principal com:
```bash
python main.py
```

### Menu interativo:
```
---------------
Escolha uma das opcoes abaixo
1. Port Scanner
2. DNS Lookup
3. WHOIS lookup
4. wafw00f
5. DNS Enumeration
6. Sair
---------------
```

## 🧪 Detalhes das Ferramentas

### 🔍 1. Scanner de Portas com Banner Grabbing

Este é um script em Python para realizar a varredura de portas em um host ou rede, identificando quais portas estão abertas, fechadas ou filtradas. Além disso, ele faz o banner grabbing para tentar identificar o sistema operacional ou serviço em execução na porta aberta.

#### Como Executar
```bash
python roteiro1.py
```

Você pode escolher entre:
- `single`: escaneia um único host (IPv4, IPv6 ou hostname)
- `network`: escaneia uma rede inteira

Exemplo:
```
Would you like to scan a single host or a network? (single/network): single
Enter the IP(Ipv4 or Ipv6) address or hostname of the target server/host: 192.168.1.1
Enter the starting port: 20
Enter the ending port: 100
```

Resultado esperado:
```
Port 22 - Status: Open - Service: ssh
Port 80 - Status: Open - Service: http
Port 22 - Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu - OS Detected: Linux
```

---

### 🌐 2. DNS Lookup

Resolve um domínio para IP.

#### Como Executar
No menu principal, escolha a opção `2`.

Exemplo:
```
Digite o domínio: example.com
[+] Lookup: example.com -> 93.184.216.34
```

---

### 🕵️ 3. WHOIS Lookup

Consulta os dados públicos de registro do domínio.

#### Como Executar
No menu principal, escolha a opção `3`.

Exemplo:
```
Digite o domínio: example.com
===== WHOIS Lookup =====
Domínio: example.com
Registrar: Example Registrar
Data de criação: 2003-08-13
Data de expiração: 2025-08-13
Servidores DNS: ['ns1.example.com', 'ns2.example.com']
Emails: ['admin@example.com']
```

---

### 🔐 4. WAF Detection

Usa a biblioteca `wafw00f` para identificar a presença de Web Application Firewalls.

#### Como Executar
No menu principal, escolha a opção `4`.

Exemplo:
```
Digite a URL (com http/https): https://example.com
[+] WAF Detectado: Cloudflare
```

---

### 📡 5. DNS Enumeration

Enumera possíveis subdomínios de um domínio base usando brute-force com wordlists.

#### Pré-requisito
Tenha um arquivo `wordlist.txt` na mesma pasta contendo possíveis subdomínios.

#### Como Executar
No menu principal, escolha a opção `5`.

Exemplo:
```
Digite o domínio: example.com

Subdomínios encontrados:
- mail.example.com -> 93.184.216.34
- www.example.com -> 93.184.216.34
```

## 📌 Observações
- O Scanner de Portas utiliza até 1000 threads para acelerar o processo de varredura.
- A detecção de sistema operacional é baseada no conteúdo do banner retornado pelas portas abertas.
- As ferramentas são organizadas em arquivos separados, mas integradas via `main.py`.
