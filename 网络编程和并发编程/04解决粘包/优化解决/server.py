import socket
import subprocess
import struct
import json
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8000),)

phone.listen(5)
print("server开始工作...")
# 这个循环是为了可以服务多个客户端，但是一次只能服务一个，其余来的均挂载
while True:
    conn, addr = phone.accept()
    print(addr)
    while True:
        # 1. 收到命令
        cmd = conn.recv(8096).decode('gbk')
        if cmd == 'exit':break  # 结束与之相关的客户端连接
        # 2.执行命令拿到结果
        obj = subprocess.Popen(cmd,shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()

        # 3.把命令结果返回给客户端
        # 第一步：制定固定长度的报头
        header_dict = {
            "filename": "1.txt",
            "total_size": len(stderr)+len(stdout)
        }
        header_json = json.dumps(header_dict)
        header_bytes = header_json.encode('gbk')
        # 第二步：先发送报头长度
        conn.send(struct.pack('i', len(header_bytes)))
        # 第三步: 在发送报头
        conn.send(header_bytes)
        # 把数据发送给客户端
        conn.send(stdout)
        conn.send(stderr)

    conn.close()

phone.close()
