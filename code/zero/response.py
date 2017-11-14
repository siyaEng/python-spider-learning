# -*- coding: utf-8 -*- 
import requests

url = 'http://www.baidu.com'

response = requests.get(url)

# HTTP 请求的返回状态, 比如, 200 表示成功, 400 表示失败
print(response.status_code)

# HTTP 请求中的 headers
print(response.headers)

# 从 header 中猜测的响应内容编码方式
print(response.encoding)

# 从内容中分析的编码方式(慢)
print(response.apparent_encoding)

# 响应内容的二进制形式
print(response.content)