import requests
from bs4 import BeautifulSoup

response = requests.get(url='https://www.autohome.com.cn/news/')

# response.encoding = 'gbk'
# 你以啥返回我就以啥方式做，默认是'utf-8'
response.encoding = response.apparent_encoding

# 将html转化为对象
soup = BeautifulSoup(response.text, features='html.parser')

# 在soup对象中找想要的id
target = soup.find(id="auto-channel-lazyload-article")

# 在id中找具体的li,find表示找第一个匹配的对象，find_all表示所有匹配的对象
li_list = target.find_all('li')

# li_list是列表，不是soup对象，不可以直接在li_list.find。但是可以i_list[数字].find
for i in li_list:
    # 通过a.attrs找到a标签里面的属性,返回一个字典，通过键获取值
    a = i.find('a')
    if a:
        print(a.attrs.get('href'))
        # a.find(a.first)获得第一个div里面的内容，.find('img')找到img标签，.attrs.get('src')获取img里面的src
        img = a.find(a.first).find('img')
        if img:
            print(img)
        txt = a.find('h3')
        print(txt)
