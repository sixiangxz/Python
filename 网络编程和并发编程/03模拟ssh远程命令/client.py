import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8000),)

while True:
    # 1. 发命令
    cmd = input("请输入查询指令：").strip()
    if not cmd: continue
    phone.send(cmd.encode('gbk'))


    # 拿出结果,并打印
    recv_data = phone.recv(1024).decode('gbk')
    print(recv_data)


phone.close()