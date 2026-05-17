import socket

target = "scanme.nmap.org"
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)

result = s.connect_ex((target, port))

if result == 0:
    print(f"port {port} : OPEN")
else:
    print(f"Port {port} : CLOSED")

s.close()
