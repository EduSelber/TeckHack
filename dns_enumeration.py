import socket

def dns():
    subdominios_comuns = [
        "www", "mail", "ftp", "webmail", "smtp", "vpn", "ns1", "ns2", "blog", "dev"
    ]

    domain = input("Digite o domínio: ")

    

    print("\n===== DNS Enumeration =====")
    print(f"[~] Iniciando DNS Enumeration em: {domain}")

    
    for sub in subdominios_comuns:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"[+] Encontrado: {subdomain} -> {ip}")
        except socket.gaierror:
            pass  
