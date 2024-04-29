import socket
import datetime


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_port = 2024
    try:
        server_socket.bind(('localhost', server_port))
    except OSError:
        print(f"Port {server_port} is already in use. Trying port 3033.")
        port = 3034
        server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"服务器已启动，正在等待客户端连接...")
    while True:
        conn, addr = server_socket.accept()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hostname = socket.gethostname()
        server_ip = server_socket.getsockname()[0]
        print(f"客户端({hostname})连接成功，时间为：{current_time}")
        conn.send(f"来自服务器({server_ip}) :你已连接成功。".encode())
        conn.send("来自服务器：再见！".encode())
        conn.close()


if __name__ == "__main__":
    server()