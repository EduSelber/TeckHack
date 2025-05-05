import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Lookup: {domain} -> {ip}")
    except socket.gaierror:
        print(f"[-] Não foi possível resolver: {domain}")

def dns():
    

    domain = input("Digite o domínio: ")

    print("\n===== DNS Lookup =====")
    dns_lookup(domain)



