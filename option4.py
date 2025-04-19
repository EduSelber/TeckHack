from wafw00f.main import WAFW00F


def detectar_waf():
    url = input("Digite a URL (com http/https): ")
    print(f"\n===== WAF Detection =====")
    try:
        detector = WAFW00F(url)
        result = detector.identwaf()
        if result:
            print(f"[+] WAF Detectado: {result}")
        else:
            print("[-] Nenhum WAF detectado.")
    except Exception as e:
        print(f"[-] Erro ao detectar WAF: {e}")

