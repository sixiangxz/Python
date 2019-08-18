import requests
from bs4 import BeautifulSoup
'''
爬取汽车之家信息
'''
response = requests.get(url='https://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# 你以啥返回我就以啥方式做，默认是'utf-8'
response.encoding = response.apparent_encoding

# 将html转化为对象
soup = BeautifulSoup(response.text, features='html.parser')
print(response.text)
# 在soup对象中找想要的id
target = soup.find(id="auto-channel-lazyload-article")

# 在id中找具体的li,find表示找第一个匹配的对象，find_all表示所有匹配的对象
li_list = target.find_all('li')

# li_list是列表，不是soup对象，不可以直接在li_list.find。但是可以i_list[数字].find
for i in li_list:
    # 通过a.attrs找到a标签里面的属性,返回一个字典，通过键获取值
    a = i.find('a')
    if a:
        # print(a.attrs.get('href'))
            # a.find(a.first)获得第一个div里面的内容，.find('img')找到img标签，.attrs.get('src')获取img里面的src
            # img = a.find(a.first).find('img')
        img_url = a.find('img').attrs.get('src')
        # 拼接头部
        img_url = 'https:'+img_url
        # print(img_url)
        txt = a.find('h3').text  # h3是一个对象，通过.text拿出文本
        # print(txt)


        # 保存图片
        # img_response = requests.get(url=img_url)
        # import uuid
        # file_name = str(uuid.uuid4()) + '.jpg'
        #
        # with open(file_name, 'wb') as f:
        #     f.write(img_response.content)
