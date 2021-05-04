import sys
import socket
import threading

print("A Simple Port Scanner, made by parnex.")
usage = "py portscan.py host_address start_port end_port"

if (len(sys.argv)) != 4:
    print(usage)
    sys.exit()

try:
    host_address = socket.gethostbyname(str(sys.argv[1]))  
except socket.gaierror:
    print('Error!')
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3]) 

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = s.connect_ex((host_address, port))
    if (not connection):
        print(f"[SCANNER] Port {port} Open")
    s.close()
    
for port in range(start_port, end_port+1):
    t1 = threading.Thread(target= scan, args=(port,))
    t1.start()
