import socket
import subprocess
import struct
import json
import os
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file_path = 'H:\Django\Python\Scrapy\study\网络编程\\05_FTP文件上传下载\服务端\share'
phone.bind(('127.0.0.1', 8000),)

phone.listen(5)
print("server开始工作...")
# 这个循环是为了可以服务多个客户端，但是一次只能服务一个，其余来的均挂载
while True:
    conn, addr = phone.accept()
    print(addr)
    while True:
        # 1. 收到命令 get 1.txt
        cmd = conn.recv(8096)
        if cmd == 'exit':break  # 结束与之相关的客户端连接
        # 解析命令,获取指定命令参数
        cmds = cmd.decode('gbk').split()  # ["get", '1.txt']
        filename = cmds[1]
        # 制定固定长度报头
        header_dict = {
            "filename": filename,
            "total_size": os.path.getsize('%s\%s' %(file_path, filename))
        }
        header_json = json.dumps(header_dict)
        header_bytes = header_json.encode('gbk')
        # 第二步：先发送报头长度
        conn.send(struct.pack('i', len(header_bytes)))
        # 第三步: 在发送报头
        conn.send(header_bytes)
        # 把下载的数据发送给客户端
        with open('%s\%s' %(file_path, filename), 'rb') as p:
            for line in p:
                conn.send(line)
    conn.close()

phone.close()
