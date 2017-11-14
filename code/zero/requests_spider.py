# -*- coding: utf-8 -*- 
import requests

def getHtmlText(url):
	try:
		response = requests.get(url)
		# 如果状态码不是 200, 则应发 HTTPERROR 异常
		response.raise_for_status()
		# 设置正确的编码方式
		response.encoding = response.apparent_encoding
		return response.text
	except:
		return "Something Wrong!"


url = 'http://www.baidu.com'

result = getHtmlText(url)
print(result)