import socket
import sys
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import ipaddress  

well_known_ports = {
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    443: "HTTPS",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP (Submission)",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Proxy"
}

def detect_os_from_banner(banner):
    os_patterns = {
        'Linux': ['Ubuntu', 'Debian', 'Red Hat', 'CentOS', 'Fedora'],
        'Windows': ['Windows NT', 'Microsoft Windows', 'IIS'],
        'MacOS': ['Darwin', 'Mac OS X'],
        'Apache': ['Apache', 'httpd'],
        'Nginx': ['nginx'],
        'SSH': ['OpenSSH'],
    }
    for os, patterns in os_patterns.items():
        for pattern in patterns:
            if pattern.lower() in banner.lower():
                return os
    return 'Unknown OS'

def banner_grab(ports, target, family):
    print("\nBanner Grabbing")
    for port in ports:
        try:
            s = socket.socket(family, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            banner = s.recv(1024).decode().strip()
            if banner:
                os_detected = detect_os_from_banner(banner)
                print(f"Port {port} - Banner: {banner} - OS Detected: {os_detected}")
            else:
                print(f"Port {port} - No banner available")
            s.close()
        except Exception:
            print(f"Port {port} - No banner available")
    return

def scan_port(target, port, family):
    try:
        s = socket.socket(family, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))  
        
        if result == 0:  
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = None

            if service is None:
                service = well_known_ports.get(port, "Unknown Service")
                
            s.close()
            return (port, service, "Open")  
        
        elif result == 111:  
            s.close()
            return (port, "N/A", "Closed")  
        
        s.close()
        return (port, "N/A", "Filtered")  

    except Exception:
        return None

def scanning(start_port, end_port, target, family):
    port_status = []
    with ThreadPoolExecutor(max_workers=1000) as executor:  
        ports_to_scan = range(start_port, end_port + 1)
        
        futures = []
        with tqdm(total=len(ports_to_scan), desc="Scanning Ports", ncols=100) as pbar:
            for port in ports_to_scan:
                future = executor.submit(scan_port, target, port, family)
                futures.append(future)
                pbar.update(1)
                
            for future in futures:
                result = future.result()
                if result:
                    port, service, status = result
                    port_status.append((port, service, status))
    
    print("\nPort Scan Results:")
    if not port_status:
        print("No ports found.")
        return []

    i = 0
    while i < len(port_status):
        start_port = port_status[i][0]
        service = port_status[i][1]
        status = port_status[i][2]
        end_port = start_port
        
        while (i + 1 < len(port_status) and 
               port_status[i + 1][2] == status and 
               port_status[i + 1][0] == end_port + 1):
            end_port = port_status[i + 1][0]
            i += 1
        
        if start_port == end_port:
            if service != "N/A":
                print(f"Port {start_port} - Status: {status} - Service: {service}")
            else:
                print(f"Port {start_port} - Status: {status}")
        else:
            print(f"Port {start_port}-{end_port} - Status: {status}")
        
        i += 1

    open_ports = [port for port, _, status in port_status if status == "Open"]
    return open_ports

def scan_network(network, start_port, end_port, family):
    open_ports_per_host = {}

    for ip in ipaddress.IPv4Network(network, strict=False):
        target = str(ip)
        print("\n" + "-"*20)
        print(f"Scanning host with IP: {target}")
        open_ports = scanning(start_port, end_port, target, family)
        if open_ports:
            open_ports_per_host[target] = open_ports
        print("-"*20)
    
    return open_ports_per_host

def main():
    choice = input("Would you like to scan a single host or a network? (single/network): ").lower()
    
    if choice == 'network':
        network_ip = input("Enter the network IP: ")
        subnet_mask = input("Enter the subnet mask (between 0 and 32): ")
        try:
            if not (0 <= int(subnet_mask) <= 32):
                print("Invalid subnet mask. Please enter a value between 0 and 32.")
                sys.exit(1)
        except ValueError:
            print("Invalid subnet mask. Please enter a numeric value.")
            sys.exit(1)

        network = f"{network_ip}/{subnet_mask}"
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        
        print(f'Scanning network: {network} from port {start_port} to {end_port}')
        open_ports_per_host = scan_network(network, start_port, end_port, socket.AF_INET)
        
        for host, open_ports in open_ports_per_host.items():
            print("\n" + "-"*20)
            print(f"Host {host} has open ports: {open_ports}")
            banner_grab(open_ports, host, socket.AF_INET)
            print("-"*20)
    
    elif choice == 'single':
        target = input("Enter the IP(Ipv4 or Ipv6) address or hostname of the target server/host:  ")
        
        try:
            
            addr_info = socket.getaddrinfo(target, None)
            
            
            ipv4_info = [info for info in addr_info if info[0] == socket.AF_INET]
            
            if ipv4_info:
                target_ip = ipv4_info[0][4][0]
                family = socket.AF_INET
                print(f"Resolving host {target} to IPv4: {target_ip}")
            else:
                target_ip = addr_info[0][4][0]  # Caso não haja IPv4, pegamos o IPv6
                family = socket.AF_INET6
                print(f"Resolving host {target} to IPv6: {target_ip}")
        except socket.gaierror:
            print("Invalid host or IP address")
            sys.exit(1)

        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))

        print(f'Scanning host with IP: {target_ip} from port {start_port} to {end_port}')
        open_ports = scanning(start_port, end_port, target_ip, family)
        banner_grab(open_ports, target_ip, family)
    
    else:
        print("Invalid choice.")
    
    print("Scan completed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
