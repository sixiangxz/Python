download = 'H:\Django\Python\Scrapy\study\网络编程\\05_FTP文件上传下载\服务端\share'
filename = '1.txt'
with open('%s\%s' %(download, filename), 'rb') as p:
    while p.readline():
        print(p.readline().decode('utf-8'))
