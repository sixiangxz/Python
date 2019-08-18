import socket
import struct
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8000),)

while True:
    # 1. 发命令
    cmd = input("请输入查询指令：").strip()
    if not cmd: continue
    phone.send(cmd.encode('gbk'))

    # 第一步：拿出报头
    header = phone.recv(4)
    # 第二步：从报头中解析数据描述信息，如数据的长度
    total_size = struct.unpack('i', header)[0]
    # 接收数据,知道把服务器发送的数据接收完毕
    print(total_size)
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:

        recv = phone.recv(200)
        print(recv.decode('gbk'))
        recv_size = recv_size + len(recv)
        print('-------------------------', recv_size)
        print(recv_data.decode('gbk'))


phone.close()