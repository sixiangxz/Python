import subprocess
while True:
    cmd = input("....:")
    print(cmd)
    obj = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    print(obj.stdout.read().decode('gbk'))
    print(obj.stderr.read().decode('gbk'))