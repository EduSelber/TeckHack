import socket
import sys
import os
from concurrent.futures import ThreadPoolExecutor


def banner_grab(ports, target):
    print("\nBanner Grabbing")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            banner = s.recv(1024)
            print(f"Port {port} - {banner.decode().strip()}")
            s.close()
        except:
            print(f"Port {port} - No banner available")
    return 


def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        
        result = s.connect_ex((target, port))  
        
        if result == 0:  
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"
            s.close()
            return (port, service, "Open")  
        
        elif result == 111:  
            s.close()
            return (port, "N/A", "Closed")  
        
        s.close()
        return (port, "N/A", "Filtered")  

    except Exception as e:
        return None
    s.close()
    return None


def scanning(start_port, end_port, target):
    port_status = []
    with ThreadPoolExecutor(max_workers=100) as executor:  
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
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


def is_host_reachable(target):
    try:
        response = os.system(f"ping -c 1 {target} > /dev/null 2>&1")
        return response == 0
    except:
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 roteiro1.py <ip_or_hostname>")
        sys.exit(1)

    target = sys.argv[1]

    try:
        target_ip = socket.gethostbyname(target)
        print(f"Resolving host {target} to IP {target_ip}")
    except socket.gaierror:
        print("Invalid host or IP address")
        sys.exit(1)

    if not is_host_reachable(target_ip):
        print(f"Host {target_ip} is unreachable")
        sys.exit(1)

    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for the ports.")
        sys.exit(1)

    print(f'Scanning host with IP: {target_ip} from port {start_port} to {end_port}')
    open_ports = scanning(start_port, end_port, target_ip)
    banner_grab(open_ports, target_ip)
    
    print("Scan completed.")
    sys.exit(0)
    return 
    
if __name__ == "__main__":
    main()
