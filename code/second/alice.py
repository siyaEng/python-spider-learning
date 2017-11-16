# coding: utf-8
import bs4

#首先我们先将 html 文件已 lxml 的方式做成一锅汤
soup = bs4.BeautifulSoup(open('alice.html'),'lxml')

#我们把结果输出一下，是一个很清晰的树形结构。
print(soup.prettify())