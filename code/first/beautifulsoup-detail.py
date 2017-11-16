# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html, "html.parser")

# 找到文件的 title
print(soup.title)

# title 的 name 值
print(soup.title.name)

# title 中的字符串 string
print(soup.title.string)

# title 的父节点的 name 属性
print(soup.title.parent.name)

# 文档的第一个找到的段落
print(soup.p)

# 找到的 p 的 class 的属性值
print(soup.p['class'])

# 找到第一个 a 标签
print(soup.a)

# 找到所有的 a 标签 新版本的 Beautiful 的写法是 find_all
print(soup.find_all('a'))

# 找到 id 值等于 3 的 a 标签
print(soup.find(id="link3"))