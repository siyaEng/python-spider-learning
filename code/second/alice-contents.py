# coding: utf-8
import bs4

#首先我们先将 html 文件已 lxml 的方式做成一锅汤
soup = bs4.BeautifulSoup(open('alice.html'),'lxml')

# contents 内容返回结果是一个 list

print(soup.head.contents)
# 输出结果 [<title>The Dormouse's story</title>]

print(soup.head.contents[0])
# 输出结果 <title>The Dormouse's story</title>

print(soup.head.contents[0].contents)
# 输出结果 [The Dormouse's story]