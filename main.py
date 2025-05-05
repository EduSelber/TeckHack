import roteiro1
import dns_lookup
import whois_lookup
import option4
import dns_enumeration

def main():
    print('-'*15)
    
    print("Escolha uma das opcoes abaixo")

    print("1. Port Scanner")
    print("2. DNS Lookup")
    print("3. WHOIS lookup")
    print("4. wafw00f")
    print("5. DNS Enumeration")
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
    if choice == "5":
        dns_enumeration.dns()
        main()
        
    if choice == "6":
        return    
if __name__ == "__main__":
    main()