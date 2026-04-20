import socket
import threading
import json

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
#grab hostname and ip address of the server machine
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listening(client_conn, client_addr):
    print(f"Connected by {client_addr}")
    #print the address of the client that just connected to the server
    with client_conn:
        while True:
            data = client_conn.recv(65536)
            if not data:
                break
            #decodesx and prints data from client 
            rdata= data.decode('utf-8').strip()
            if not rdata:
                continue

            print(f"{client_addr}: {rdata}")
            http_response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 7\r\nConnection: close\r\n\r\nAFFIRM!"
            client_conn.sendall(str.encode(http_response))

def start_server():
    server_socket.bind((host_ip, 6666))
    server_socket.listen(10)


    print(f"server on, up and listening on {host_ip}:6666")

    
    while True:
        client_conn, client_addr = server_socket.accept()
        server_thread = threading.Thread(target= listening, args=(client_conn, client_addr))
        server_thread.daemon = True
        server_thread.start()


if __name__ == "__main__":
    
    start_server()
