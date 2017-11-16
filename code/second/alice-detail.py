# coding: utf-8
import bs4

#首先我们先将 html 文件已 lxml 的方式做成一锅汤
soup = bs4.BeautifulSoup(open('alice.html'),'lxml')

# 获取 head 标签内的内容
#print(soup.head)
# 输出结果 <head><title>The Dormouse's story</title></head>

# 获取 title 标签内的内容
#print(soup.title) 
# 输出结果 <title>The Dormouse's story</title>


# 如果你还想更深入的获得更小的tag：例如我们想找到body下的被b标签包裹的部分
#print(soup.body.b)
# 输出结果 <b>The Dormouse's story</b>

# 获取所有 a 标签
tagA = soup.find_all('a')
print(tagA)
# 获取第一个 a 标签
print(tagA[0])