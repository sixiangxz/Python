import socket
import subprocess
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8000),)

phone.listen(5)
conn, addr = phone.accept()
print("server开始工作...")
while True:
    # 收到命令
    cmd = conn.recv(8096).decode('gbk')
    if not cmd:break
    obj = subprocess.Popen(cmd,shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    stdout = obj.stdout.read()
    stderr = obj.stderr.read()
    conn.send(stdout)
    conn.send(stderr)

conn.close()
conn.close()
