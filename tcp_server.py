import socket
import threading
IP = '0.0.0.0'
PORT = 9998


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5) # 연결 허용 최댓값
    print(f'[*] Listening on {IP}:{PORT}')
    while True:
        client, address = server.accept() # clinet: 소켓, address: 원격 연결 관련 세부 정보 포함
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACKKK')


if __name__ == '__main__':
    main()