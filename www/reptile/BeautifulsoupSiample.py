# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import bs4
'用来解析内容'
class BeautifulsoupSiample(object):
    html = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>
        <a class="story">...</a>
        """
    def number1(self):

        soup=BeautifulSoup(self.html,"html.parser")
        print soup.title
        print soup.title.string
        print soup.p.attrs
        print soup.p['name']
        aString=soup.a.string
        print type(aString)
        if type(aString)==(bs4.element.Comment):#注释
            print aString

        for content in soup.body.contents:
            print "------------------"
            print type(content)
            print content

        print soup.body.contents[0]#可以用下标访问



        print soup.body.children
        '''
        #只遍历子节点
        for content in soup.body.contents:
            print content
        for child in soup.body.children:
            print child
        '''
        for child in soup.head.descendants:
            print "------------------"
            print child
            print "------------------"

        #关键字 后面加下划线 limit 限制检索条数
        allP= soup.find_all("p",class_="story",limit=2)
        allP=soup.select("p.story")#注意属性和标签属于同一节点，所以中间不能加空格
        allP=soup.select('p[class="story"]')
        for p in allP:
            print p



    #print soup.head
        #print soup.a
    pass

bf=BeautifulsoupSiample()
bf.number1()