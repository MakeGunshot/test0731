# coding=utf-8

import requests

print('requests post示例')
# 目标url
url = 'http://httpbin.org/post'
# 请求数据
data = {'data_1':'xxx','data_2':'ccc'}
# 发送post请求
r = requests.post(url,data=data)
# 输出结果
print(r.text)



