# coding: utf-8
import bs4

#首先我们先将 html 文件已 lxml 的方式做成一锅汤
soup = bs4.BeautifulSoup(open('alice.html'),'lxml')

for string in soup.strings:
    print(repr(string))