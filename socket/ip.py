import socket

#获得本机ip地址
local_ip = socket.gethostbyname(socket.gethostname())
print(f"本机IP地址：{local_ip}")

# 获取用户输入的循环次数
n = int(input("请输入待查询服务器URL数量："))

# 使用for循环来执行指定次数的循环
for i in range(n):
    server_url = input("请输入服务器URL地址：")
    # 获取服务器ip地址
    server_ip = socket.gethostbyname(server_url)
    print(f"{server_url}对应的ip地址是：{server_ip}")
    i += 1






