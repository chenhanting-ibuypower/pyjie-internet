# coding:utf-8
import requests

my_data = {'name': 'yujie', 'birthday': '800521'}
response = requests.post('http://localhost:8000/', data = my_data)

print("text =", response.text)
print("status_code =", response.status_code)
print("headers =", response.headers)



