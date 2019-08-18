import socket
import struct
import json
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
download = 'H:\Django\Python\Scrapy\study\网络编程\\05_FTP文件上传下载\客户端\下载'
phone.connect(('127.0.0.1', 8000),)

while True:
    # 1. 发命令
    cmd = input("请输入要下载的文件名(exit即退出):").strip()
    if not cmd: continue
    if cmd == 'exit':
        phone.send(cmd.encode('gbk'))
        break
    phone.send(cmd.encode('gbk'))

    # 第一步：拿出报头
    header = phone.recv(4)
    # 第二步：获取整个字典长度
    header_size = struct.unpack('i', header)[0]
    print(header_size)
    # 一次接受整个字典长度大小
    header_json = phone.recv(header_size).decode('gbk')
    # 通过字典的键获取值
    header_dict = json.loads(header_json)
    total_size = header_dict['total_size']
    # 获取下载文件名
    filename = header_dict['filename']
    # 接收数据，并保存到本地
    with open('%s\%s' %(download, filename), 'wb') as p:
        recv_size = 0
        while recv_size < total_size:

            line = phone.recv(1024)
            p.write(line)
            recv_size = recv_size + len(line)
            print("总大小：%s   已下载大小：%s" % (total_size,recv_size))

phone.close()