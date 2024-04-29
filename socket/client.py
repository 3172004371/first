import socket


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 2024)
    # 连接到服务器
    client_socket.connect(server_address)
    server_info = client_socket.recv(1024).decode()
    print(server_info)
    second_message = client_socket.recv(1024).decode()
    print(second_message)
    client_socket.close()


if __name__ == "__main__":
    client()