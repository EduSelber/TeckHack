import socket
import sys
from tqdm import tqdm  

def banner_grab(ports):
    print("Banner Grabbing")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, port))
            banner = s.recv(1024)
            print(f"Port {port} - {banner}")
            s.close()
        except:
            print(f"Port {port} - No banner available")
    return 

def scanning(start_port, end_port, target):
    try:
        open_ports = []
        for port in tqdm(range(start_port, end_port + 1), desc="Scanning", unit="port"):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            if s.connect_ex((target, port)) == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown Service"
                open_ports.append(port)
                print(f'Port {port} is open - Service: {service}')
            
            s.close()
        return open_ports
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print("\nError:", e)
        sys.exit(1)
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
    banner_grab(open_ports)
    print("Scan completed.")
    sys.exit(0)
    return 
if __name__ == "__main__":
    main()