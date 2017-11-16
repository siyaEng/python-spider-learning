# coding: utf-8
import bs4


#首先我们先将html文件已lxml的方式做成一锅汤
soup = bs4.BeautifulSoup(open('alice.html'),'lxml')

#我们把结果输出一下，是一个很清晰的树形结构。
#print(soup.prettify())

# print(soup.head)

# print(soup.head.contents)

# print(soup.title)

# print(soup.body.b)

# tagA = soup.find_all('a')
# print(tagA)

# print(tagA[1])

# titleTag = soup.title

# for child in titleTag.children:
# 	print(child)

# for child in soup.head.descendants:
# 	print(child)

for string in soup.strings:
	print(repr(string))