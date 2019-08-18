import struct
# i表示整数，即4个字节。
# 即通过pack把数据压缩为定长的4个字节,数字最大长度不超过四个字节表示范围
length = 1024
header = struct.pack('i', length)
print(header)


# 通过unpack把数据还原
data = struct.unpack('i', header)[0]
print(data)


# 此做法缺点1.报头信息太少 2.发送的数据长度不能超过4个字节,当传输文件时不号
