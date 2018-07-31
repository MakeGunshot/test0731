
# encoding =utf-8
import requests

print('requests自定义请求头基本示例')
url = 'http://www.baidu.com'
# 定义自定义请求头数据
headers = {
    'user-agent':'XXXX'
}
# 发送带自动以头的请求
r = requests.get(url,headers=headers)