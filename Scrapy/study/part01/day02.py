import requests

form_data2 = {

    'password': 'xxxxxxxx',
    'phone': '18351547549',
}

# response = requests.post(
#     url="https://dig.chouti.com/login",
#     data=form_data2
# )
response = requests.get(
    url="https://dig.chouti.com/",
)
print(response.cookies)
