import roteiro1
import dns_lookup
import whois_lookup
import option4

def main():
    print('-'*15)
    print("Escolha uma das opcoes abaixo")

    print("1. Port Scanner")
    print("2. DNS Lookup e DNS Enumeration")
    print("3. WHOIS lookup")
    print("4. wafw00f")
    print("6. Sair")
    print('-'*15)
    choice = input("Escolha: ")
    if choice == "1":
        roteiro1.port_scanner()
        main()
    if choice == "2":
        dns_lookup.dns()
        main()
    if choice == "3":
        whois_lookup.whois_lookup()
        main()    
    if choice == "4":
        option4.detectar_waf()
        main()
    if choice == "6":
        return    
if __name__ == "__main__":
    main()