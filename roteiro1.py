import socket
import sys
from tqdm import tqdm  
from concurrent.futures import ThreadPoolExecutor, as_completed

def banner_grab(ports, target):
    print("\nBanner Grabbing")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
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
        s.settimeout(0.1)
        if s.connect_ex((target, port)) == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"
            s.close()
            return (port, service)
    except Exception as e:
        return None
    s.close()
    return None

def scanning(start_port, end_port, target):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:  # Define o número de threads
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        for future in tqdm(as_completed(futures), total=len(futures), desc="Scanning", unit="port"):
            result = future.result()
            if result:
                port, service = result
                open_ports.append(port)
                print(f'Port {port} is open - Service: {service}')
    return open_ports

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 roteiro1.py <ip>")
        sys.exit(1)

    target = sys.argv[1]

    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Please enter a valid range between 1 and 65535.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter numeric values for the ports.")
        sys.exit(1)

    print(f'Scanning host with IP: {target} from port {start_port} to {end_port}')
    open_ports = scanning(start_port, end_port, target)
    banner_grab(open_ports, target)
    print("Scan completed.")
    sys.exit(0)
    return 
    
if __name__ == "__main__":
    main()
