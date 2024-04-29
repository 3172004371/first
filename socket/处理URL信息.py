from urllib.parse import urlparse


def parse_url(url):
    # 解析URL
    parsed_url = urlparse(url)

    # 提取协议名、主机名和端口号
    protocol = parsed_url.scheme
    hostname = parsed_url.hostname
    port = parsed_url.port

    # 如果端口号不存在，则使用默认端口号
    if not port:
        if protocol == 'http':
            port = 80
        elif protocol == 'https':
            port = 443

    return protocol, hostname, port


def main():
    # 输入URL地址
    url = input("请输入URL地址：")

    # 调用函数解析URL
    protocol, hostname, port = parse_url(url)

    # 显示解析结果
    print("协议名：", protocol)
    print("主机名：", hostname)
    print("端口号：", port)


if __name__ == "__main__":
    main()