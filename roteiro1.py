import socket
import sys
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm 

def banner_grab(ports, target, family):
    print("\nBanner Grabbing")
    for port in ports:
        try:
            s = socket.socket(family, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            banner = s.recv(1024)
            print(f"Port {port} - {banner.decode().strip()}")
            s.close()
        except:
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

def is_host_reachable(target, family):
    try:
        if family == socket.AF_INET6:
            response = os.system(f"ping6 -c 1 {target} > /dev/null 2>&1")
        else:
            response = os.system(f"ping -c 1 {target} > /dev/null 2>&1")
        return response == 0
    except:
        return False

def main():
    target = input("Enter the IP address or hostname of the target server/host:  ")
    family = None
    target_ip = None

    try:
        addr_info = socket.getaddrinfo(target, None)
        target_ip = addr_info[0][4][0]
        family = addr_info[0][0]
        print(f"Resolving host {target} to IP {target_ip}")
    except socket.gaierror:
        print("Invalid host or IP address")
        sys.exit(1)

    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for the ports.")
        sys.exit(1)

    print(f'Scanning host with IP: {target_ip} from port {start_port} to {end_port}')
    open_ports = scanning(start_port, end_port, target_ip, family)
    banner_grab(open_ports, target_ip, family)
    
    print("Scan completed.")
    sys.exit(0)
    
if __name__ == "__main__":
    main()
