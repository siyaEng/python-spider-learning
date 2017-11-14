# -*- coding: utf-8 -*- 
import requests

url = 'http://baidu.com'

proxy = {
	#'http': 'http://127.0.0.1:1080',
	#'https': 'https://127.0.0.1:1080',
	# 这里我用的是 sock5 协议的代理
	'sock5': 'http://127.0.0.1:1080'
}
response = requests.get(url, proxies=proxy)

print(response.content)