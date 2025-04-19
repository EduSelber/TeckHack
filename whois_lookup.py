import whois

def whois_lookup():
    domain = input("Digite o domínio: ")
    try:
        info = whois.whois(domain)
        print("\n===== WHOIS Lookup =====")
        print(f"Domínio: {domain}")
        print(f"Registrar: {info.registrar}")
        print(f"Data de criação: {info.creation_date}")
        print(f"Data de expiração: {info.expiration_date}")
        print(f"Servidores DNS: {info.name_servers}")
        print(f"Emails: {info.emails}")
    except Exception as e:
        print(f"[-] Erro ao fazer WHOIS lookup: {e}")


