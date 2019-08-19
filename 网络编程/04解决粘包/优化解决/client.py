import socket
import struct
import json
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8000),)

while True:
    # 1. 发命令
    cmd = input("请输入查询指令(exit即退出)").strip()
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
    recv_dict = phone.recv(header_size).decode('gbk')
    # 通过键获取值
    total_size = json.loads(recv_dict)['total_size']

    recv_size = 0
    recv_data = b''
    while recv_size < total_size:

        recv = phone.recv(200)
        print(recv.decode('gbk'))
        recv_size = recv_size + len(recv)
        print('-------------------------', recv_size)
        print(recv_data.decode('gbk'))


phone.close()