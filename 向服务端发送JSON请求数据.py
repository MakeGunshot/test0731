
# coding = utf-8

import requests

print('requests posp json 数据示例')
# 目标URL
url = 'http://jsonpalceholder.typicode.com/posts'
# 请求头中一定要标识一下content-type
headers = {'Content-Type':'application/json'}
# 请求数据
json_data = {'data_1':'xxx','data_2':'ccc'}

# 发送post请求
r = requests.post(url,json=json_data,headers=headers)
# 打印返回结果
print(r.text)



