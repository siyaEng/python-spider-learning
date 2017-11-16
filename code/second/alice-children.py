# coding: utf-8
import bs4

#首先我们先将 html 文件已 lxml 的方式做成一锅汤
soup = bs4.BeautifulSoup(open('alice.html'),'lxml')

# 通过 tag 的 .children 生成器，可以对 tag 的子节点进行循环
for child in soup.title.children:
    print(child)
# 输出结果 The Dormouse's story

# 遍历孙子节点
for child in soup.head.descendants:
    print(child)
# 输出结果为 
# <title>The Dormouse's story</title>
# The Dormouse's story