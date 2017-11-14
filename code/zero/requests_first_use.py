# -*- coding: utf-8 -*- 
# 先导入 requests 包
import requests

# 抓取来自百度的首页, 并用变量 response 保存
# 注意这里, 网页前面的 http://一定要写出来, 它并不能像真正的浏览器一样帮我们补全 http 协议

url = "http://www.baidu.com"
response = requests.get(url)

# 将获取到的内容打印出来
print(response.content)