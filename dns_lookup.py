import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Lookup: {domain} -> {ip}")
    except socket.gaierror:
        print(f"[-] Não foi possível resolver: {domain}")

def dns():
    subdominios_comuns = [
        "www", "mail", "ftp", "webmail", "smtp", "vpn", "ns1", "ns2", "blog", "dev"
    ]

    domain = input("Digite o domínio: ")

    print("\n===== DNS Lookup =====")
    dns_lookup(domain)

    print("\n===== DNS Enumeration =====")
    print(f"[~] Iniciando DNS Enumeration em: {domain}")

    
    for sub in subdominios_comuns:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"[+] Encontrado: {subdomain} -> {ip}")
        except socket.gaierror:
            pass  


