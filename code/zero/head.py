import requests

head = {'User-agent': '123'}
url = 'http://baidu.com'
response = requests.get(url, headers=head)

print(response.request.headers)