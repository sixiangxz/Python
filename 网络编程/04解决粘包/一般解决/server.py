import socket
import subprocess
import struct
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8000),)

phone.listen(5)
conn, addr = phone.accept()
print("server开始工作...")
while True:
    # 1. 收到命令
    cmd = conn.recv(8096).decode('gbk')
    if not cmd:break
    # 2.执行命令拿到结果
    obj = subprocess.Popen(cmd,shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    stdout = obj.stdout.read()
    stderr = obj.stderr.read()

    # 3.把命令结果返回给客户端
    # 第一步：制定固定长度的报头
    total_size = len(stdout) + len(stderr)
    header = struct.pack('i', total_size)
    # 第二步：把报头返回给客户端
    conn.send(header)
    # 把数据发送给客户端
    conn.send(stdout)
    conn.send(stderr)

conn.close()
conn.close()
